import pygame
from modelos.coordenada import Coordenada
from modelos.boton import Boton
from constantes import *
from funciones.auxiliares import calcular_centro_horizontal, calcular_centro_vertical

# Menu Principal
class MenuPrincipal:
    def __init__(self, ventana: pygame.Surface):
        self.ventana = ventana
        self.ventana_actual = VENTANA_MENU_PRINCIPAL
        self.menu_contenedor = pygame.image.load(MENU_CONTENEDOR_PATH)
        self.botones = []
        self.posicion = Coordenada(0, 0)
        self.crear_botones()

    def crear_botones(self):
        self.botones.append(Boton('Jugar', Coordenada(VENTANA_CENTRO_WIDTH, 100)))
        self.botones.append(Boton('Rankings', Coordenada(VENTANA_CENTRO_WIDTH, 175)))
        self.botones.append(Boton('Estadisticas', Coordenada(VENTANA_CENTRO_WIDTH, 250)))
        self.botones.append(Boton('Configuracion', Coordenada(VENTANA_CENTRO_WIDTH, 325)))
        self.botones.append(Boton('Salir', Coordenada(VENTANA_CENTRO_WIDTH, 400)))

    def renderizar(self):
        # Renderizar background
        self.renderizar_background()

        # Renderizar contenedor
        self.renderizar_contenedor()
        
        # Agregar titulo
        self.renderizar_titulo()

        # Agregar botones
        self.renderizar_botones()

        # Posicionar menu
        self.posicion.x = calcular_centro_horizontal(self.ventana, self.menu_contenedor)
        self.posicion.y = calcular_centro_vertical(self.ventana, self.menu_contenedor)
        
        # Renderizar menu
        self.ventana.blit(self.menu_contenedor, (self.posicion.x, self.posicion.y))

    def renderizar_background(self):
        background = pygame.transform.scale(BACKGROUND_MENU_PRINCIPAL, VENTANA_MEDIDA)
        self.ventana.blit(background, (0, 0))

    def renderizar_contenedor(self):
        self.menu_contenedor = pygame.transform.scale(self.menu_contenedor, (500, 600))

    def renderizar_titulo(self):
        text = FUENTE_30.render(MENU_PRINCIPAL_TITULO, True, MENU_PRINCIPAL_TITULO_COLOR)
        text_sombra = FUENTE_30.render(MENU_PRINCIPAL_TITULO, True, MENU_PRINCIPAL_TITULO_COLOR_SOMBRA)
        self.menu_contenedor.blit(text_sombra, (calcular_centro_horizontal(self.menu_contenedor, text) + 2, 82))
        self.menu_contenedor.blit(text, (calcular_centro_horizontal(self.menu_contenedor, text), 80))

    def renderizar_botones(self):
        for boton in self.botones:
            posicion_x = calcular_centro_horizontal(self.menu_contenedor, boton.imagen)
            posicion_y = boton.posicion.y + 50
            boton.rectangulo = self.menu_contenedor.blit(boton.imagen, (posicion_x, posicion_y))

    def ejecutar(self, cola_eventos: list[pygame.event.Event], ventana_actual: str) -> str:
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

        for boton in self.botones:
            boton_rect = boton.obtener_rectangulo(self.menu_contenedor, self.posicion)
            
            if mouse_rect.colliderect(boton_rect):
                boton.disparar_efecto_hover()
            else:
                boton.remover_efecto_hover()

    def manejar_evento_click(self, evento: pygame.event.Event):
        for boton in self.botones:
            boton_rect = boton.obtener_rectangulo(self.menu_contenedor, self.posicion)
            if boton_rect.collidepoint(evento.pos):
                if boton.label == "Salir":
                    self.ventana_actual = VENTANA_SALIR
                elif boton.label == "Jugar":
                    self.ventana_actual = VENTANA_JUGAR
                elif boton.label == "Rankings":
                    self.ventana_actual = VENTANA_RANKING
                elif boton.label == "Estadisticas":
                    self.ventana_actual = VENTANA_ESTADISTICAS
                elif boton.label == "Configuracion":
                    self.ventana_actual = VENTANA_CONFIGURACION
