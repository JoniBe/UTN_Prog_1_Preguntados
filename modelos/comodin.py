import pygame
from constantes import *
from funciones.auxiliares import calcular_centro_horizontal
from modelos.coordenada import Coordenada

# Comodin
class Comodin:
    def __init__(self, tipo_comodin: str, posicion: Coordenada):
        self.tipo = tipo_comodin
        self.posicion = posicion
        self.surface = None
        self.surface_original = None
        self.rectangulo = None
        self.cantidad = 0
        self.utilizado = False
        self.crear_comodin()

    def crear_comodin(self):
        comodin = None
        cantidad = None
        posicion_y = None
        self.surface = CONTENEDOR_COMODIN.copy()
        if self.tipo == COMODIN_TIPO_BOMBA:
            cantidad = CANTIDAD_COMODIN_BOMBA
            comodin = COMODIN_BOMBA.copy()
            posicion_y = 20
        elif self.tipo == COMODIN_TIPO_PASAR:
            cantidad = CANTIDAD_COMODIN_PASAR
            comodin = COMODIN_PASAR.copy()
            posicion_y = 25
        elif self.tipo == COMODIN_TIPO_X2:
            cantidad = CANTIDAD_COMODIN_X2
            comodin = COMODIN_X2.copy()
            posicion_y = 15
        elif self.tipo == COMODIN_TIPO_DOBLE_CHANCE:
            cantidad = CANTIDAD_COMODIN_DOBLE_CHANCE
            comodin = COMODIN_DOBLE_CHANCE.copy()
            posicion_y = 15
        posicion_x = calcular_centro_horizontal(self.surface, comodin)
        self.cantidad = cantidad
        self.surface.blit(comodin, (posicion_x, posicion_y)) 
        self.surface_original = self.surface.copy()
        self.renderizar_cantidad()

    def renderizar_cantidad(self):
        cantidad = FUENTE_20.render(str(self.cantidad), False, COLOR_NEGRO)
        self.surface.blit(cantidad, (15, 10))

    def disparar_efecto_hover(self):
        if self.cantidad > 0 and not self.utilizado:
            self.surface = self.surface_original.copy()
            brillo = pygame.Surface(self.surface.get_size(), pygame.SRCALPHA)
            brillo.fill((30, 30, 30, 0))
            self.surface.blit(brillo, (0, 0), special_flags=pygame.BLEND_RGB_ADD)
            self.renderizar_cantidad()

    def remover_efecto_hover(self):
        self.surface = self.surface_original.copy()
        if self.cantidad == 0 or self.utilizado:
            brillo = pygame.Surface(self.surface.get_size(), pygame.SRCALPHA)
            brillo.fill((60, 60, 60, 255))
            self.surface.blit(brillo, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
        self.renderizar_cantidad()
    
    def actualizar_cantidad(self):
        if self.cantidad > 0:
            self.cantidad -= 1
            self.surface = self.surface_original.copy()
            self.renderizar_cantidad()