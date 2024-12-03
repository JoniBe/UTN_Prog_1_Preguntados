import pygame
from constantes import *
from funciones.auxiliares import calcular_centro_horizontal, calcular_centro_vertical
from modelos.boton import Boton
from modelos.coordenada import Coordenada

# Configuracion
class Configuracion:
    def __init__(self, ventana: pygame.Surface):
        self.ventana = ventana
        self.ventana_actual = VENTANA_CONFIGURACION
        self.boton_volver = Boton('Volver', Coordenada(0, 720), 'CONFIGURACION')
        self.botones_de_volumen: list[Boton] = []
        self.volumen_actual = 100
        self.crear_botones_de_volumen()

    def renderizar_background(self):
        background = pygame.transform.scale(BACKGROUND_CONFIGURACION, VENTANA_MEDIDA)
        self.ventana.blit(background, (0, 0))

    def renderizar_titulo(self):
        text = FUENTE_30.render(CONFIGURACION_TITULO, True, CONFIGURACION_TITULO_COLOR)
        text_sombra = FUENTE_30.render(CONFIGURACION_TITULO, True, CONFIGURACION_TITULO_COLOR_SOMBRA)
        self.ventana.blit(text_sombra, (calcular_centro_horizontal(self.ventana, text) + 2, 42))
        self.ventana.blit(text, (calcular_centro_horizontal(self.ventana, text), 40))

    def crear_botones_de_volumen(self):
        self.botones_de_volumen = []
        boton_volumen_menos = Boton("MENO", Coordenada(100, 100), BOTON_TIPO_VOLUMEN, BOTON_VOLUMEN_MENOS)
        boton_volumen_mas = Boton("MAS", Coordenada(600, 100), BOTON_TIPO_VOLUMEN, BOTON_VOLUMEN_MAS)
        boton_volumen_mutear = Boton("MUTEAR", Coordenada(100, 200), BOTON_TIPO_VOLUMEN, BOTON_VOLUMEN_MUTEAR)
        boton_volumen_desmutear = Boton("DESMUTEAR", Coordenada(600, 200), BOTON_TIPO_VOLUMEN, BOTON_VOLUMEN_DESMUTEAR)
        self.botones_de_volumen.extend([boton_volumen_menos, boton_volumen_mas, boton_volumen_mutear, boton_volumen_desmutear])

    def renderizar_control_volumen(self):
        for boton in self.botones_de_volumen:
            boton.rectangulo = self.ventana.blit(boton.imagen, (boton.posicion.x, boton.posicion.y))
        
    def renderizar_barra_volumen(self):        
        # Creo rectangulo base de la barra
        barra_base = pygame.Surface((300, 30))
        barra_base.fill((100, 100, 100))
        
        # Creo rectangulo de nivel de volumen
        ancho_nivel = int(300 * self.volumen_actual / 100)
        barra_nivel = pygame.Surface((ancho_nivel, 30))
        barra_nivel.fill((64, 174, 120))
        
        # Barra base
        posicion_x = calcular_centro_horizontal(self.ventana, barra_base)
        self.ventana.blit(barra_base, (posicion_x, 120))
        
        # Nivel de volumen
        self.ventana.blit(barra_nivel, (posicion_x, 120))

        # Border negro
        pygame.draw.rect(self.ventana, COLOR_NEGRO, (posicion_x, 120, 300, 30), 2)
        
        # Muestro porcentaje
        texto = FUENTE_20.render(f"{self.volumen_actual}%", True, COLOR_BLANCO)
        self.ventana.blit(texto, (calcular_centro_horizontal(self.ventana, texto), 125))

    def renderizar_boton_volver(self):
        posicion_x = calcular_centro_horizontal(self.ventana, self.boton_volver.imagen)
        self.boton_volver.rectangulo = self.ventana.blit(self.boton_volver.imagen, (posicion_x, self.boton_volver.posicion.y))
    
    def renderizar(self):
        self.renderizar_background()
        self.renderizar_titulo()
        self.renderizar_control_volumen()
        self.renderizar_barra_volumen()
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

        # Hover Botones de Volumen
        for boton in self.botones_de_volumen:
            boton_rect = boton.rectangulo
            if mouse_rect.colliderect(boton_rect):
                boton.disparar_efecto_hover()
            else:
                boton.remover_efecto_hover()

    def manejar_evento_click(self, evento: pygame.event.Event):
        boton_rect = self.boton_volver.rectangulo
        # Click Boton Volver
        if boton_rect.collidepoint(evento.pos):
            if self.boton_volver.label == "Volver":
                self.ventana_actual = VENTANA_MENU_PRINCIPAL
                return
        
        # Click Botones de Volumen
        for boton in self.botones_de_volumen:
            boton_rect = boton.rectangulo
            if boton_rect.collidepoint(evento.pos):
                if boton.label == "MUTEAR":
                    pygame.mixer.music.pause()
                elif boton.label == "DESMUTEAR":
                    pygame.mixer.music.unpause()
                elif boton.label == "MENO":
                    self.setear_volumen(self.volumen_actual - 10)
                elif boton.label == "MAS":
                    self.setear_volumen(self.volumen_actual + 10)

    def setear_volumen(self, volumen: int):
        if volumen < 0:
            volumen = 0
        elif volumen > 100:
            volumen = 100

        self.volumen_actual = volumen
        pygame.mixer.music.set_volume(volumen / 100)

    