import pygame
from constantes import *
from modelos.boton import Boton
from modelos.campo import Campo
from modelos.coordenada import Coordenada
from funciones.auxiliares import calcular_centro_horizontal

# Customizar
class Customizar:
    def __init__(self, ventana: pygame.Surface):
        self.ventana = ventana
        self.ventana_actual = VENTANA_CUSTOMIZAR
        self.boton_volver = Boton('Volver', Coordenada(0, 720), 'CUSTOMIZAR')
        self.puntos_ganados = '0'
        self.puntos_perdidos = '0'
        self.vidas = '0'
        self.tiempo = '0'
        self.campo_puntos_ganados = None
        self.campo_puntos_perdidos = None
        self.campo_vidas = None
        self.campo_tiempo = None

    def renderizar_background(self):
        background = pygame.transform.scale(BACKGROUND_CUSTOMIZAR, VENTANA_MEDIDA)
        self.ventana.blit(background, (0, 0))

    def renderizar_titulo(self):
        text = FUENTE_30.render(CUSTOMIZAR_TITULO, True, CUSTOMIZAR_TITULO_COLOR)
        text_sombra = FUENTE_30.render(CUSTOMIZAR_TITULO, True, CUSTOMIZAR_TITULO_COLOR_SOMBRA)
        self.ventana.blit(text_sombra, (calcular_centro_horizontal(self.ventana, text) + 2, 42))
        self.ventana.blit(text, (calcular_centro_horizontal(self.ventana, text), 40))

    def renderizar_boton_volver(self):
        posicion_x = calcular_centro_horizontal(self.ventana, self.boton_volver.imagen)
        self.boton_volver.rectangulo = self.ventana.blit(self.boton_volver.imagen, (posicion_x, self.boton_volver.posicion.y))

    def renderizar_campo_puntos_ganados(self):
        # Renderizar label
        campo_puntos_ganados_titulo = FUENTE_16.render("Puntos ganados:", False, COLOR_NEGRO)
        campo_puntos_ganados_titulo_sombra = FUENTE_16.render("Puntos ganados:", False, COLOR_BLANCO)
        self.ventana.blit(campo_puntos_ganados_titulo_sombra, (22, 100))
        self.ventana.blit(campo_puntos_ganados_titulo, (20, 100))
        # Renderizar campo
        campo_puntos_ganados = Campo(self.puntos_ganados, Coordenada(20, 125), FUENTE_20, CAMPO_CUSTOMIZAR)
        campo_puntos_ganados.rectangulo = self.ventana.blit(campo_puntos_ganados.imagen, (campo_puntos_ganados.posicion.x, campo_puntos_ganados.posicion.y))
        self.campo_puntos_ganados = campo_puntos_ganados

    def renderizar_campo_puntos_perdidos(self):
        # Renderizar label
        campo_puntos_perdidos_titulo = FUENTE_16.render("Puntos perdidos:", False, COLOR_NEGRO)
        campo_puntos_perdidos_titulo_sombra = FUENTE_16.render("Puntos perdidos:", False, COLOR_BLANCO)
        self.ventana.blit(campo_puntos_perdidos_titulo_sombra, (522, 100))
        self.ventana.blit(campo_puntos_perdidos_titulo, (520, 100))
        # Renderizar campo
        campo_puntos_perdidos = Campo(self.puntos_perdidos, Coordenada(520, 125), FUENTE_20, CAMPO_CUSTOMIZAR)
        campo_puntos_perdidos.rectangulo = self.ventana.blit(campo_puntos_perdidos.imagen, (campo_puntos_perdidos.posicion.x, campo_puntos_perdidos.posicion.y))
        self.campo_puntos_perdidos = campo_puntos_perdidos

    def renderizar_campo_vidas(self):
        # Renderizar label
        campo_vidas_titulo = FUENTE_16.render("Vidas:", False, COLOR_NEGRO)
        campo_vidas_titulo_sombra = FUENTE_16.render("Vidas:", False, COLOR_BLANCO)
        self.ventana.blit(campo_vidas_titulo_sombra, (22, 225))
        self.ventana.blit(campo_vidas_titulo, (20, 225))
        # Renderizar campo
        campo_vidas = Campo(self.vidas, Coordenada(20, 250), FUENTE_20, CAMPO_CUSTOMIZAR)
        campo_vidas.rectangulo = self.ventana.blit(campo_vidas.imagen, (campo_vidas.posicion.x, campo_vidas.posicion.y))
        self.campo_vidas = campo_vidas

    def renderizar_campo_tiempo(self):
        # Renderizar label
        campo_tiempo_titulo = FUENTE_16.render("Tiempo:", False, COLOR_NEGRO)
        campo_tiempo_titulo_sombra = FUENTE_16.render("Tiempo:", False, COLOR_BLANCO)
        self.ventana.blit(campo_tiempo_titulo_sombra, (522, 225))
        self.ventana.blit(campo_tiempo_titulo, (520, 225))
        # Renderizar campo
        campo_tiempo = Campo(self.tiempo, Coordenada(520, 250), FUENTE_16, CAMPO_CUSTOMIZAR)
        campo_tiempo.rectangulo = self.ventana.blit(campo_tiempo.imagen, (campo_tiempo.posicion.x, campo_tiempo.posicion.y))
        self.campo_tiempo = campo_tiempo

    def renderizar_campos_de_customizacion(self):
        self.renderizar_campo_puntos_ganados()
        self.renderizar_campo_puntos_perdidos()
        self.renderizar_campo_vidas()
        self.renderizar_campo_tiempo()
    
    def renderizar(self):
        self.renderizar_background()
        self.renderizar_titulo()
        self.renderizar_campos_de_customizacion()
        self.renderizar_boton_volver()

    def mostrar(self, cola_eventos: list[pygame.event.Event], ventana_actual: str) -> str:
        self.ventana_actual = ventana_actual

        for evento in cola_eventos:
            if evento.type == pygame.QUIT:
                self.ventana_actual = VENTANA_SALIR
            elif evento.type == pygame.MOUSEMOTION:
                self.manejar_hover_de_botones(evento)
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                self.manejar_evento_click(evento)

        self.renderizar()

        return self.ventana_actual
    
    def manejar_hover_de_botones(self, evento: pygame.event.Event) -> bool:
        mouse_rect = pygame.Rect(evento.pos, [1,1])

        # Hover Boton Volver
        boton_rect = self.boton_volver.rectangulo
        if mouse_rect.colliderect(boton_rect):
            self.boton_volver.disparar_efecto_hover()
        else:
            self.boton_volver.remover_efecto_hover()

    def manejar_evento_click(self, evento: pygame.event.Event):
        boton_rect = self.boton_volver.rectangulo
        # Click Boton Volver
        if boton_rect.collidepoint(evento.pos):
            if self.boton_volver.label == "Volver":
                self.ventana_actual = VENTANA_MENU_PRINCIPAL
                return