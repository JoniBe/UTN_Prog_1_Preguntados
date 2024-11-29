import pygame
import random
from modelos.coordenada import Coordenada
from modelos.boton import Boton
from Constantes import *
from funciones.auxiliares import calcular_centro_horizontal, calcular_centro_vertical
from funciones.manejo_archivos import leer_csv_preguntas
from Funciones import mostrar_pregunta_en_contenedor, reproducir_sonido

pygame.init()
pygame.mixer.init()

# Partida
class Partida:
    def __init__(self, ventana: pygame.Surface):
        self.ventana = ventana
        self.ventana_actual = VENTANA_JUGAR
        self.puntuacion = 0
        self.vidas = CANTIDAD_VIDAS
        self.usuario = ""
        self.acertados_seguidos = 1
        self.tiempo = TIEMPO_INICIAL
        self.preguntas = []
        self.botones = []
        self.posicion = Coordenada(0,0)
        self.evento_tiempo_1s = pygame.USEREVENT
        self.cargar_preguntas()
        pygame.time.set_timer(self.evento_tiempo_1s, 1000)
    
    def cargar_preguntas(self):
        self.preguntas = leer_csv_preguntas()
        self.sortear_lista_preguntas()

    def sortear_lista_preguntas(self):
        random.shuffle(self.preguntas)

    def renderizar_botones(self):
        pregunta_actual = self.preguntas[0]

        posicion_y_inicial = 380
        self.botones = []
        for opcion in pregunta_actual.opciones:
            self.botones.append(Boton(opcion, Coordenada(VENTANA_CENTRO_WIDTH, posicion_y_inicial), "JUEGO"))
            posicion_y_inicial += 80

        for boton in self.botones:
            boton.rectangulo = self.ventana.blit(boton.imagen, (boton.posicion.x, boton.posicion.y))

    def renderizar_pregunta(self):
        contenedor_pregunta = CONTENEDOR_PREGUNTA.copy()
        mostrar_pregunta_en_contenedor(contenedor_pregunta, self.preguntas[0].pregunta)
        self.ventana.blit(contenedor_pregunta, (100, 140))

    def renderizar_tiempo(self):
        contenedor_tiempo = CONTENEDOR_TIEMPO.copy()
        contenedor_tiempo = pygame.transform.scale(contenedor_tiempo, (64, 64))
        tiempo_restante = FUENTE_20.render(str(self.tiempo), False, COLOR_AZUL)
        posicion_x = calcular_centro_horizontal(contenedor_tiempo, tiempo_restante)
        posicion_y = calcular_centro_vertical(contenedor_tiempo, tiempo_restante)
        contenedor_tiempo.blit(tiempo_restante, (posicion_x, posicion_y))
        self.ventana.blit(contenedor_tiempo, (700, 10))

    def renderizar_vidas(self):
        contenedor_vidas = CONTENEDOR_VIDAS.copy()
        contenedor_vidas = pygame.transform.scale(contenedor_vidas, (140, 64))
        tiempo_restante = FUENTE_20.render(f"VIDAS: {self.vidas}", False, COLOR_AZUL)
        posicion_x = calcular_centro_horizontal(contenedor_vidas, tiempo_restante)
        posicion_y = calcular_centro_vertical(contenedor_vidas, tiempo_restante)
        contenedor_vidas.blit(tiempo_restante, (posicion_x, posicion_y))
        self.ventana.blit(contenedor_vidas, (40, 10))

    def renderizar_puntuacion(self):
        contenedor_puntuacion = CONTENEDOR_PUNTUACION.copy()
        contenedor_puntuacion = pygame.transform.scale(contenedor_puntuacion, (280, 64))
        puntuacion = FUENTE_20.render(f"PUNTUACION: {self.puntuacion}", False, COLOR_AZUL)
        posicion_x = calcular_centro_horizontal(contenedor_puntuacion, puntuacion)
        posicion_y = calcular_centro_vertical(contenedor_puntuacion, puntuacion)
        contenedor_puntuacion.blit(puntuacion, (posicion_x, posicion_y))
        self.ventana.blit(contenedor_puntuacion, (300, 10))

    def renderizar_fondo(self):
        fondo_juego = pygame.transform.scale(BACKGROUND_PARTIDA, VENTANA_MEDIDA)
        self.ventana.blit(fondo_juego, (0,0))
        
    def renderizar(self):
        # Renderizar fondo
        self.renderizar_fondo()

        # Agregar botones
        self.renderizar_botones()

        # Mostrar pregunta
        self.renderizar_pregunta()

        # Renderizar tiempo
        self.renderizar_tiempo()

        # Renderizar vidas
        self.renderizar_vidas()

        # Renderizar puntuacion
        self.renderizar_puntuacion()

        # Renderizar la partida
        self.posicion.x = calcular_centro_horizontal(self.ventana, self.ventana)
        self.posicion.y = calcular_centro_vertical(self.ventana, self.ventana)        
        self.ventana.blit(self.ventana, (self.posicion.x, self.posicion.y))

    def ejecutar(self, cola_eventos: list[pygame.event.Event]) -> str:
        retorno = self.ventana_actual

        if self.vidas == 0:
            self.ventana_actual = VENTANA_FIN_PARTIDA
        else:
            self.ventana_actual = VENTANA_JUGAR
        
        for evento in cola_eventos:
            if evento.type == pygame.QUIT:
                retorno = VENTANA_SALIR
            if evento.type == self.evento_tiempo_1s:
                self.tiempo -= 1
                if self.tiempo <= 0:
                    retorno = VENTANA_FIN_PARTIDA
            if evento.type == pygame.MOUSEBUTTONDOWN:
                self.manejar_evento_click(evento)

        self.renderizar()

        return retorno

    def manejar_evento_click(self, evento: pygame.event.Event):
        for i in range(len(self.botones)):
            if self.botones[i].rectangulo.collidepoint(evento.pos):
                respuesta_seleccionada = i + 1
                self.gestionar_puntuacion(respuesta_seleccionada)
                self.sortear_lista_preguntas()
                break

    def gestionar_puntuacion(self, respuesta_seleccionada: int):
        pregunta_actual = self.preguntas[0]

        if pregunta_actual.validar_respuesta(respuesta_seleccionada):
            reproducir_sonido(SONIDO_ACIERTO)
            self.puntuacion += PUNTUACION_ACIERTO
            self.acertados_seguidos += 1

            if self.acertados_seguidos == MAX_ACIERTOS_SEGUIDOS:
                self.vidas += VIDA_EXTRA_POR_ACIERTOS_SEGUIDOS
                self.tiempo += TIEMPO_EXTRA_POR_ACIERTOS_SEGUIDOS

            if self.acertados_seguidos > 4:
                self.acertados_seguidos = 0
        else:
            reproducir_sonido(SONIDO_ERROR)
            self.puntuacion -= PUNTUACION_ERROR
            self.vidas -= 1
            self.acertados_seguidos = 0