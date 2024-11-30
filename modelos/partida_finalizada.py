import pygame
from constantes import *
from modelos.campo import Campo
from modelos.boton import Boton
from modelos.coordenada import Coordenada
from modelos.partida import Partida
from funciones.auxiliares import calcular_centro_horizontal, calcular_centro_vertical
from Funciones import obtener_fecha, generar_json

# PARTIDA FINALIZADA
class PartidaFinalizada:
    def __init__(self, ventana: pygame.Surface):
        self.ventana = ventana
        self.ventana_actual = VENTANA_PARTIDA_FINALIZADA
        self.partida_actual = None
        self.usuario = ''
        self.boton_aceptar = Boton('ACEPTAR', Coordenada(VENTANA_CENTRO_WIDTH, 500), "JUEGO")
        self.campo_usuario_activo = False

    def renderizar_fondo(self):
        fondo_juego = pygame.transform.scale(BACKGROUND_PARTIDA_TERMINADA, VENTANA_MEDIDA)
        self.ventana.blit(fondo_juego, (0,0))

    def renderizar_puntuacion(self):
        if self.partida_actual:
            # Renderizar titulo
            puntuacion_titulo = FUENTE_30.render("Usted ha obtenido:", False, COLOR_BLANCO)
            self.ventana.blit(puntuacion_titulo, (calcular_centro_horizontal(self.ventana, puntuacion_titulo), 100))
            # Renderizar contenedor puntuacion
            contenedor_puntuacion = CONTENEDOR_PUNTUACION.copy()
            contenedor_puntuacion = pygame.transform.scale(contenedor_puntuacion, (280, 64))
            puntuacion = FUENTE_20.render(f"PUNTUACION: {self.partida_actual.puntuacion}", False, COLOR_AZUL)
            posicion_x = calcular_centro_horizontal(contenedor_puntuacion, puntuacion)
            posicion_y = calcular_centro_vertical(contenedor_puntuacion, puntuacion)
            contenedor_puntuacion.blit(puntuacion, (posicion_x, posicion_y))
            self.ventana.blit(contenedor_puntuacion, (calcular_centro_horizontal(self.ventana, contenedor_puntuacion), 160))

    def renderizar_campo_usuario(self):
        # Renderizar titulo
        campo_usuario_titulo = FUENTE_30.render("Ingrese su nombre:", False, COLOR_BLANCO)
        self.ventana.blit(campo_usuario_titulo, (calcular_centro_horizontal(self.ventana, campo_usuario_titulo), 300))
        # Renderizar campo usuario
        posicion_y = 360
        campo_usuario = Campo(self.usuario, Coordenada(VENTANA_CENTRO_WIDTH, posicion_y))
        campo_usuario.posicion.x = calcular_centro_horizontal(self.ventana, campo_usuario.imagen)
        campo_usuario.rectangulo = self.ventana.blit(campo_usuario.imagen, (campo_usuario.posicion.x, campo_usuario.posicion.y))
        self.campo_usuario = campo_usuario
    
    def renderizar_boton_aceptar(self):
        self.boton_aceptar.rectangulo = self.ventana.blit(self.boton_aceptar.imagen, (self.boton_aceptar.posicion.x, self.boton_aceptar.posicion.y))

    def renderizar(self):
        # Renderizar fondo
        self.renderizar_fondo()

        # Renderizar puntuacion
        self.renderizar_puntuacion()

        # Renderizar campo y texto usuario
        self.renderizar_campo_usuario()

        # Renderizar boton Aceptar
        self.renderizar_boton_aceptar()

    def manejar_evento_hover(self, evento: pygame.event.Event) -> bool:
        mouse_rect = pygame.Rect(evento.pos, [1,1])

        boton_rect = self.boton_aceptar.rectangulo
        if mouse_rect.colliderect(boton_rect):
            self.boton_aceptar.disparar_efecto_hover()
        else:
            self.boton_aceptar.remover_efecto_hover()
           

    def manejar_evento_click(self, evento: pygame.event.Event):
         # Manejar click en boton ACEPTAR -> Guardamos info en JSON
        if self.boton_aceptar and self.usuario != '' and self.boton_aceptar.rectangulo.collidepoint(evento.pos):
            self.guardar_puntuacion()
            self.partida_actual.resetear_partida()
            self.resetear_valores()
            self.ventana_actual = VENTANA_MENU_PRINCIPAL

        # Manejar click en CAMPO USUARIO
        if self.campo_usuario and self.campo_usuario.rectangulo.collidepoint(evento.pos):
            self.campo_usuario_activo = True
        else:
            self.campo_usuario_activo = False

    def manejar_evento_tecla(self, evento: pygame.event.Event):
        if self.campo_usuario_activo:
            letra_presionada = str(evento.unicode)
            if evento.key == pygame.K_BACKSPACE:
                self.usuario = self.usuario[:-1]
            elif letra_presionada and len(self.usuario) < 20 and not(evento.key == pygame.K_BACKSPACE):
                self.usuario += letra_presionada

    def guardar_puntuacion(self):
        lista_puntuacion = []
        informacion = {
            "puntos": self.partida_actual.puntuacion,
            "fecha": obtener_fecha(),
            "nombre": self.usuario
        }
        lista_puntuacion.append(informacion)
        generar_json("puntos.json", lista_puntuacion, self.usuario)

    def mostrar(self, cola_eventos: list[pygame.event.Event], ventana_actual: str, partida: Partida) -> str:
        self.ventana_actual = ventana_actual
        self.partida_actual = partida

        for evento in cola_eventos:
            if evento.type == pygame.QUIT:
                self.ventana_actual = VENTANA_SALIR
            elif evento.type == pygame.MOUSEMOTION:
                self.manejar_evento_hover(evento)
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                self.manejar_evento_click(evento)
            elif evento.type == pygame.KEYDOWN:
                self.manejar_evento_tecla(evento)

        self.renderizar()

        return self.ventana_actual
    
    def resetear_valores(self):
        self.partida_actual = None
        self.usuario = ''
        self.campo_usuario_activo = False