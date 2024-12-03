import pygame
from constantes import *
from modelos.boton import Boton
from modelos.coordenada import Coordenada
from funciones.auxiliares import calcular_centro_horizontal, calcular_centro_vertical
from funciones.manejo_archivos import leer_csv_preguntas

# Estadisticas
class Estadisticas:
    def __init__(self, ventana: pygame.Surface):
        self.ventana = ventana
        self.ventana_actual = VENTANA_ESTADISTICAS
        self.contenedor = None
        self.boton_volver = Boton('Volver', Coordenada(0, 740), 'ESTADISTICAS')
        self.headers = ["PREGUNTAS", "ACIERTOS", "FALLOS", "PORCENTAJE DE ACIERTOS"]
        self.preguntas_por_pagina = 7
        self.pagina_actual = 0
        self.boton_anterior = Boton('Anterior', Coordenada(50, 670), 'ESTADISTICAS')
        self.boton_siguiente = Boton('Siguiente', Coordenada(500, 670), 'ESTADISTICAS')

    def renderizar_background(self):
        background = pygame.transform.scale(BACKGROUND_RANKING, VENTANA_MEDIDA)
        self.ventana.blit(background, (0, 0))

    def renderizar_contenedor(self):
        # Renderiza el contenedor
        self.contenedor = pygame.transform.scale(RANKING_CONTENEDOR, (700, 600))
        posicion_x = calcular_centro_horizontal(self.ventana, self.contenedor)
        posicion_y = 60

        # Renderiza estadisticas
        self.renderizar_estadisticas_en_contenedor()

        # Agrega el contenedor a la ventana
        self.ventana.blit(self.contenedor, (posicion_x, posicion_y))

    def renderizar_estadisticas_en_contenedor(self):
        listado_preguntas = leer_csv_preguntas()
        inicio = self.pagina_actual * self.preguntas_por_pagina
        fin = inicio + self.preguntas_por_pagina
        preguntas_pagina = listado_preguntas[inicio:fin]
        posicion_y = 84

        for pregunta in preguntas_pagina:
            posicion_x = 44
            # Pregunta
            texto_pregunta = FUENTE_12.render(f"{pregunta.pregunta}", True, COLOR_NEGRO)
            self.contenedor.blit(texto_pregunta, (posicion_x, posicion_y))

            # Acierto
            texto_aciertos = FUENTE_12.render(f"ACIERTOS: {pregunta.cantidad_de_aciertos}", True, COLOR_NEGRO)
            self.contenedor.blit(texto_aciertos, (posicion_x, posicion_y + 20))    

            # Fallos
            texto_fallos = FUENTE_12.render(f"FALLOS: {pregunta.cantidad_de_fallos}", True, COLOR_NEGRO)
            self.contenedor.blit(texto_fallos, (posicion_x + 240, posicion_y + 20))

            # Porcentaje de aciertos
            texto_porcentaje_aciertos = FUENTE_12.render(f"% DE ACIERTOS: {pregunta.porcentaje_de_aciertos}", True, COLOR_NEGRO)
            self.contenedor.blit(texto_porcentaje_aciertos, (posicion_x + 440, posicion_y + 20))

            posicion_y += 60

        total_paginas = (len(listado_preguntas) + self.preguntas_por_pagina - 1) // self.preguntas_por_pagina
        texto_pagina = FUENTE_12.render(f"Página {self.pagina_actual + 1} de {total_paginas}", True, COLOR_NEGRO)
        self.contenedor.blit(texto_pagina, (300, 550))
            
    def renderizar_titulo(self):
        text = FUENTE_30.render(ESTADISTICAS_TITULO, True, ESTADISTICAS_TITULO_COLOR)
        text_sombra = FUENTE_30.render(ESTADISTICAS_TITULO, True, ESTADISTICAS_TITULO_COLOR_SOMBRA)
        self.ventana.blit(text_sombra, (calcular_centro_horizontal(self.ventana, text) + 2, 22))
        self.ventana.blit(text, (calcular_centro_horizontal(self.ventana, text), 20))

    def renderizar_boton_volver(self):
        posicion_x = calcular_centro_horizontal(self.ventana, self.boton_volver.imagen)
        self.boton_volver.rectangulo = self.ventana.blit(self.boton_volver.imagen, (posicion_x, self.boton_volver.posicion.y))
    
    def renderizar_botones_paginacion(self):
        listado_preguntas = leer_csv_preguntas()
        total_paginas = (len(listado_preguntas) + self.preguntas_por_pagina - 1) // self.preguntas_por_pagina
        
        if self.pagina_actual > 0:
            self.boton_anterior.rectangulo = self.ventana.blit(self.boton_anterior.imagen, (self.boton_anterior.posicion.x, self.boton_anterior.posicion.y))
            
        if self.pagina_actual < total_paginas - 1:
            self.boton_siguiente.rectangulo = self.ventana.blit(self.boton_siguiente.imagen, (self.boton_siguiente.posicion.x, self.boton_siguiente.posicion.y))

    def renderizar(self):
        self.renderizar_background()
        self.renderizar_contenedor()
        self.renderizar_titulo()
        self.renderizar_boton_volver()
        self.renderizar_botones_paginacion()
        
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
        
        for boton in [self.boton_volver, self.boton_anterior, self.boton_siguiente]:
            if boton.rectangulo and mouse_rect.colliderect(boton.rectangulo):
                boton.disparar_efecto_hover()
            else:
                boton.remover_efecto_hover()

    def manejar_evento_click(self, evento: pygame.event.Event):
        listado_preguntas = leer_csv_preguntas()
        total_paginas = (len(listado_preguntas) + self.preguntas_por_pagina - 1) // self.preguntas_por_pagina

        if self.boton_volver.rectangulo.collidepoint(evento.pos):
            if self.boton_volver.label == "Volver":
                self.ventana_actual = VENTANA_MENU_PRINCIPAL
        elif (self.boton_anterior.rectangulo and 
              self.boton_anterior.rectangulo.collidepoint(evento.pos) and 
              self.pagina_actual > 0):
            self.pagina_actual -= 1
        elif (self.boton_siguiente.rectangulo and 
              self.boton_siguiente.rectangulo.collidepoint(evento.pos) and 
              self.pagina_actual < total_paginas - 1):
            self.pagina_actual += 1
