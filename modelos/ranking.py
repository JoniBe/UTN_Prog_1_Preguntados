import pygame
from constantes import *
from modelos.boton import Boton
from modelos.coordenada import Coordenada
from funciones.auxiliares import calcular_centro_horizontal, calcular_centro_vertical
from funciones.manejo_archivos import leer_json_ranking

# Ranking
class Ranking:
    def __init__(self, ventana: pygame.Surface):
        self.ventana = ventana
        self.ventana_actual = VENTANA_RANKING
        self.contenedor = None
        self.boton_volver = Boton('Volver', Coordenada(0, 720), 'RANKING')
        self.headers = ["POSICION", "PUNTAJE", "NOMBRE", "FECHA"]

    def renderizar_background(self):
        background = pygame.transform.scale(BACKGROUND_RANKING, VENTANA_MEDIDA)
        self.ventana.blit(background, (0, 0))

    def renderizar_contenedor_con_top_10(self):
        # Renderiza el contenedor
        self.contenedor = pygame.transform.scale(RANKING_CONTENEDOR, (700, 600))
        posicion_x = calcular_centro_horizontal(self.ventana, self.contenedor)
        posicion_y = calcular_centro_vertical(self.ventana, self.contenedor)

        # Renderizar header
        self.renderizar_header_en_contenedor()

        # Renderiza el top 10
        self.renderizar_top_10_en_contenedor()

        # Agrega el contenedor a la ventana
        self.ventana.blit(self.contenedor, (posicion_x, posicion_y))

    def renderizar_header_en_contenedor(self):
        posicion_y = 100
        posicion_x = 60
        for header in self.headers:
            text = FUENTE_16.render(header, True, COLOR_NEGRO)
            self.contenedor.blit(text, (posicion_x, posicion_y))
            posicion_x += 160

    def renderizar_top_10_en_contenedor(self):
        lista_ranking = leer_json_ranking()
        lista_ranking.sort(key=lambda x: x.puntos, reverse=True)
        max_index = min(10, len(lista_ranking))
        for i in range(max_index):
            ranking_aux = lista_ranking[i]
            
            posicion_y = 130 + i * 30
            posicion_x = 60

            texto_posicion = FUENTE_16.render(f"{i+1}", True, COLOR_NEGRO)
            self.contenedor.blit(texto_posicion, (posicion_x, posicion_y))

            texto_puntaje = FUENTE_16.render(f"{ranking_aux.puntos}", True, COLOR_NEGRO)
            self.contenedor.blit(texto_puntaje, (posicion_x + 160, posicion_y))    
            texto_nombre = FUENTE_16.render(f"{ranking_aux.nombre}", True, COLOR_NEGRO)
            self.contenedor.blit(texto_nombre, (posicion_x + 320, posicion_y))
            texto_fecha = FUENTE_16.render(f"{ranking_aux.fecha}", True, COLOR_NEGRO)
            self.contenedor.blit(texto_fecha, (posicion_x + 480, posicion_y))

    def renderizar_titulo(self):
        text = FUENTE_30.render(RANKING_TITULO, True, RANKING_TITULO_COLOR)
        text_sombra = FUENTE_30.render(RANKING_TITULO, True, RANKING_TITULO_COLOR_SOMBRA)
        self.ventana.blit(text_sombra, (calcular_centro_horizontal(self.ventana, text) + 2, 42))
        self.ventana.blit(text, (calcular_centro_horizontal(self.ventana, text), 40))

    def renderizar_boton_volver(self):
        posicion_x = calcular_centro_horizontal(self.ventana, self.boton_volver.imagen)
        self.boton_volver.rectangulo = self.ventana.blit(self.boton_volver.imagen, (posicion_x, self.boton_volver.posicion.y))
    
    def renderizar(self):
        self.renderizar_background()
        self.renderizar_contenedor_con_top_10()
        self.renderizar_titulo()
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
        boton_rect = self.boton_volver.rectangulo
        if mouse_rect.colliderect(boton_rect):
            self.boton_volver.disparar_efecto_hover()
        else:
            self.boton_volver.remover_efecto_hover()

    def manejar_evento_click(self, evento: pygame.event.Event):
        boton_rect = self.boton_volver.rectangulo
        if boton_rect.collidepoint(evento.pos):
            if self.boton_volver.label == "Volver":
                self.ventana_actual = VENTANA_MENU_PRINCIPAL
