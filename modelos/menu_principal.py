import pygame
from modelos.coordenada import Coordenada
from modelos.boton import Boton
from Constantes import *
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
        self.botones.append(Boton('Configuracion', Coordenada(VENTANA_CENTRO_WIDTH, 200)))
        self.botones.append(Boton('Salir', Coordenada(VENTANA_CENTRO_WIDTH, 300)))

    def renderizar(self):
        # Renderizar background
        self.renderizar_background()

        # Escalar menu
        self.menu_contenedor = pygame.transform.scale(self.menu_contenedor, (500, 500))
        
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
                self.ventana_actual = self.manejar_evento_click(evento)

        self.renderizar()

        return self.ventana_actual

        # for evento in cola_eventos:
        #     if evento.type == pygame.QUIT:
        #         retorno = VENTANA_SALIR
        #     elif evento.type == pygame.MOUSEBUTTONDOWN:
        #         for i in range(len(self.botones)):
        #             if self.botones[i].rectangulo.collidepoint(evento.pos):
        #                 CLICK_SONIDO.play()
        #             if i == BOTON_JUGAR:
        #                 retorno = "juego"
        #             elif i == BOTON_CONFIG:
        #                 retorno = "configuraciones"
        #             elif i == BOTON_RANKINGS:
        #                 retorno = "rankings"
        #             elif i == BOTON_SALIR:
        #                 retorno = "salir"
        
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
                    return VENTANA_SALIR
                elif boton.label == "Jugar":
                    return VENTANA_JUGAR
        return VENTANA_MENU_PRINCIPAL
