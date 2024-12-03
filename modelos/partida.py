import pygame
import random
from modelos.coordenada import Coordenada
from modelos.boton import Boton
from modelos.comodin import Comodin
from constantes import *
from funciones.auxiliares import calcular_centro_horizontal, calcular_centro_vertical
from funciones.manejo_archivos import leer_csv_preguntas, actualizar_csv_de_preguntas
from funciones.componentes import mostrar_texto_en_contenedor
from funciones.auxiliares import reproducir_sonido

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
        self.acertados_seguidos = 0
        self.tiempo = TIEMPO_INICIAL
        self.preguntas = []
        self.campo_usuario = None
        self.campo_usuario_activo = False
        self.boton_aceptar = None
        self.posicion = Coordenada(0,0)
        self.evento_tiempo_1s = pygame.USEREVENT
        self.indice_pregunta = 0
        self.cargar_preguntas()
        self.botones_respuestas: list[Boton] = []
        self.botones_comodines: list[Comodin] = []
        self.crear_comodines()
        pygame.time.set_timer(self.evento_tiempo_1s, 1000)
    
    def cargar_preguntas(self):
        self.preguntas = leer_csv_preguntas()
        self.sortear_lista_preguntas()

    def sortear_lista_preguntas(self):
        random.shuffle(self.preguntas)

    def renderizar_pregunta(self):
        contenedor_pregunta = CONTENEDOR_PREGUNTA.copy()
        mostrar_texto_en_contenedor(contenedor_pregunta, self.preguntas[self.indice_pregunta].pregunta)
        self.ventana.blit(contenedor_pregunta, (100, 140))

    def renderizar_respuestas(self):
        self.botones_respuestas = []
        pregunta_actual = self.preguntas[self.indice_pregunta]
        posicion_y_inicial = 380

        for opcion in pregunta_actual.respuestas:
            if not opcion.esconder:
                boton = Boton(opcion.respuesta, Coordenada(VENTANA_CENTRO_WIDTH, posicion_y_inicial), BOTON_TIPO_RESPUESTA)
                posicion_x = calcular_centro_horizontal(self.ventana, boton.imagen)
                boton.posicion.x = posicion_x
                posicion_y_inicial += 80
                boton.rectangulo = self.ventana.blit(boton.imagen, (boton.posicion.x, boton.posicion.y))
                self.botones_respuestas.append(boton)

    def crear_comodines(self):
        self.botones_comodines = []
        comodin_bomba = Comodin(COMODIN_TIPO_BOMBA, Coordenada(120, 700))
        self.botones_comodines.append(comodin_bomba)
        comodin_x2 = Comodin(COMODIN_TIPO_X2, Coordenada(270, 700))
        self.botones_comodines.append(comodin_x2)
        comodin_pasar = Comodin(COMODIN_TIPO_PASAR, Coordenada(420, 700))
        self.botones_comodines.append(comodin_pasar)
        comodin_doble_chance = Comodin(COMODIN_TIPO_DOBLE_CHANCE, Coordenada(570, 700))
        self.botones_comodines.append(comodin_doble_chance)

    def renderizar_comodines(self):
        for comodin in self.botones_comodines:
            comodin.rectangulo = self.ventana.blit(comodin.surface, (comodin.posicion.x, comodin.posicion.y))

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
        self.ventana.blit(contenedor_puntuacion, (calcular_centro_horizontal(self.ventana, contenedor_puntuacion), 10))

    def renderizar_fondo(self):
        fondo_juego = pygame.transform.scale(BACKGROUND_PARTIDA, VENTANA_MEDIDA)
        self.ventana.blit(fondo_juego, (0,0))
        
    def renderizar(self):
        # Renderizar fondo
        self.renderizar_fondo()

        # Mostrar pregunta
        self.renderizar_pregunta()

        # Agregar botones
        self.renderizar_respuestas()

        # Renderizar comodines
        self.renderizar_comodines()

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

    def jugar(self, cola_eventos: list[pygame.event.Event], ventana_actual: str) -> str:
        self.ventana_actual = ventana_actual

        if self.vidas == 0 or self.tiempo <= 0:
            self.ventana_actual = VENTANA_PARTIDA_FINALIZADA
        else:
            self.ventana_actual = VENTANA_JUGAR 

        for evento in cola_eventos:
            if evento.type == pygame.QUIT:
                self.ventana_actual = VENTANA_SALIR
            elif evento.type == self.evento_tiempo_1s:
                self.tiempo -= 1
            elif evento.type == pygame.MOUSEMOTION:
                self.manejar_hover_de_botones(evento)
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                self.manejar_evento_click(evento)

        self.renderizar()

        return self.ventana_actual
    
    def manejar_hover_de_botones(self, evento: pygame.event.Event) -> bool:
        mouse_rect = pygame.Rect(evento.pos, [1,1])

        for boton in self.botones_respuestas:
            boton_rect = boton.rectangulo
            if mouse_rect.colliderect(boton_rect):
                boton.disparar_efecto_hover()
            else:
                boton.remover_efecto_hover()

        for comodin in self.botones_comodines:
            if mouse_rect.colliderect(comodin.rectangulo):
                comodin.disparar_efecto_hover()
            else:
                comodin.remover_efecto_hover()

    def manejar_evento_click(self, evento: pygame.event.Event):
        # Manejar click en botones de respuestas
        for i in range(len(self.botones_respuestas)):
            if self.botones_respuestas[i].rectangulo.collidepoint(evento.pos):
                # Verificar si comodin doble chance está activo.
                tiene_doble_chance = self.verificar_si_comodin_esta_activo(COMODIN_TIPO_DOBLE_CHANCE)

                respuesta_seleccionada = self.botones_respuestas[i].label
                self.gestionar_puntuacion(respuesta_seleccionada, tiene_doble_chance)
                
                self.resetear_comodines()
                return
        
        # Manejar click en comodines
        for i in range(len(self.botones_comodines)):
            comodin_actual = self.botones_comodines[i]
            if comodin_actual.rectangulo.collidepoint(evento.pos):
                if comodin_actual.cantidad > 0 and not comodin_actual.utilizado:
                    comodin_actual.utilizado = True
                    if comodin_actual.tipo == COMODIN_TIPO_BOMBA:
                        self.disparar_comodin_bomba()
                    elif comodin_actual.tipo == COMODIN_TIPO_PASAR:
                        self.disparar_comodin_pasar()
                    elif comodin_actual.tipo == COMODIN_TIPO_X2 or comodin_actual.tipo == COMODIN_TIPO_DOBLE_CHANCE:
                        reproducir_sonido(SONIDO_COMODIN)
                    comodin_actual.actualizar_cantidad()
                return

    def resetear_comodines(self):
        for comodin in self.botones_comodines:
            comodin.utilizado = False

    def disparar_comodin_bomba(self):
        reproducir_sonido(SONIDO_EXPLOSION)

        pregunta_actual = self.preguntas[self.indice_pregunta]

        respuestas_incorrectas = []
        for i in range(len(pregunta_actual.respuestas)):
            respuesta_actual = pregunta_actual.respuestas[i]
            if not pregunta_actual.validar_respuesta(respuesta_actual.respuesta):
                respuestas_incorrectas.append(i)

        respuesta_a_eliminar = random.choice(respuestas_incorrectas)
        pregunta_actual.respuestas[respuesta_a_eliminar].esconder = True

        respuesta_a_eliminar_2 = random.choice(respuestas_incorrectas)
        while respuesta_a_eliminar == respuesta_a_eliminar_2:
            respuesta_a_eliminar_2 = random.choice(respuestas_incorrectas)
        pregunta_actual.respuestas[respuesta_a_eliminar_2].esconder = True

    def disparar_comodin_pasar(self):
        reproducir_sonido(SONIDO_COMODIN)
        self.pasar_a_siguiente_pregunta()
        self.resetear_comodines()

    def gestionar_puntuacion(self, respuesta_seleccionada: str, tiene_doble_chance: bool):
        pregunta_actual = self.preguntas[self.indice_pregunta]

        es_acierto = pregunta_actual.validar_respuesta(respuesta_seleccionada)

        if es_acierto:
            reproducir_sonido(SONIDO_ACIERTO)

            # Verificar si comodin x2 está activo, si es así, multiplicar la puntuación por 2
            tiene_x2 = self.verificar_si_comodin_esta_activo(COMODIN_TIPO_X2)
            if tiene_x2:
                self.puntuacion += PUNTUACION_ACIERTO * 2
            else:
                self.puntuacion += PUNTUACION_ACIERTO

            self.acertados_seguidos += 1

            if self.acertados_seguidos == MAX_ACIERTOS_SEGUIDOS:
                self.vidas += VIDA_EXTRA_POR_ACIERTOS_SEGUIDOS
                self.tiempo += TIEMPO_EXTRA_POR_ACIERTOS_SEGUIDOS
                self.acertados_seguidos = 0
            
            self.pasar_a_siguiente_pregunta()
        else:
            reproducir_sonido(SONIDO_ERROR)

            if not tiene_doble_chance:
                self.puntuacion -= PUNTUACION_ERROR
                self.vidas -= 1
                self.acertados_seguidos = 0
                self.pasar_a_siguiente_pregunta()
        
        # Calcular contadores de pregunta
        pregunta_actual.recalcular_contadores(es_acierto)

        # Actualizar archivo csv
        actualizar_csv_de_preguntas(self.preguntas)

    def verificar_si_comodin_esta_activo(self, tipo_comodin: str) -> bool:
        for i in range(len(self.botones_comodines)):
            comodin_actual = self.botones_comodines[i]
            if comodin_actual.tipo == tipo_comodin and comodin_actual.utilizado:
                return True
        return False
    
    def pasar_a_siguiente_pregunta(self):
        self.indice_pregunta += 1
        if self.indice_pregunta >= len(self.preguntas):
            self.sortear_lista_preguntas()
            self.indice_pregunta = 0

    def resetear_partida(self):
        self.puntuacion = 0
        self.vidas = CANTIDAD_VIDAS
        self.usuario = ""
        self.acertados_seguidos = 0
        self.tiempo = TIEMPO_INICIAL
        for comodin in self.botones_comodines:
            comodin.resetear_comodin()
