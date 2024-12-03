import pygame
from modelos.coordenada import Coordenada
from constantes import *
from funciones.auxiliares import calcular_centro_horizontal
from funciones.componentes import mostrar_texto_en_contenedor

# Campo
class Campo:
    def __init__(self, texto: str, posicion: Coordenada, fuente: pygame.font.Font = FUENTE_30, campo: pygame.Surface = CAMPO_USUARIO):
        self.imagen = campo.copy()
        self.texto = texto
        self.posicion = posicion
        self.rectangulo = None
        mostrar_texto_en_contenedor(self.imagen, self.texto, fuente)

    def obtener_rectangulo(self, contenedor: pygame.Surface, posicion_contenedor: Coordenada = None):
        boton_x = calcular_centro_horizontal(contenedor, self.imagen)
        boton_y = self.posicion.y + 50

        if posicion_contenedor:
            boton_x += posicion_contenedor.x
            boton_y += posicion_contenedor.y

        boton_width, boton_height = self.imagen.get_size()
        boton_rect = pygame.Rect(boton_x, boton_y, boton_width, boton_height)

        return boton_rect