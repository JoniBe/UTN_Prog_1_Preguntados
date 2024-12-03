import pygame
from modelos.coordenada import Coordenada
from constantes import *
from funciones.auxiliares import calcular_centro_horizontal, calcular_centro_vertical

# Boton
class Boton:
    def __init__(self, label: str, posicion: Coordenada, tipo: str = BOTON_TIPO_MENU, icono: pygame.Surface = None):
        if tipo == BOTON_TIPO_MENU:
            self.imagen = pygame.transform.scale(BOTON_VERDE, (BOTON_ESCALADO_ANCHO, BOTON_ESCALADO_ALTO))
        elif tipo == BOTON_TIPO_RESPUESTA:
            self.imagen = pygame.transform.scale(BOTON_AZUL, (BOTON_ESCALADO_ANCHO + 200, BOTON_ESCALADO_ALTO))
        elif tipo == BOTON_TIPO_VOLUMEN:
            contenedor = pygame.transform.scale(CONTENEDOR_BOTON_VOLUMEN, (75, 75))
            boton_volumen = pygame.transform.scale(icono, (50, 50))
            posicion_x = calcular_centro_horizontal(contenedor, boton_volumen)
            posicion_y = calcular_centro_vertical(contenedor, boton_volumen)
            contenedor.blit(boton_volumen, (posicion_x, posicion_y))
            self.imagen = contenedor
        else:
            self.imagen = pygame.transform.scale(BOTON_AZUL, (BOTON_ESCALADO_ANCHO, BOTON_ESCALADO_ALTO))

        self.imagen_original = self.imagen.copy()
        self.label = label
        self.posicion = posicion
        self.rectangulo = None
        self.tipo = tipo
        self.agregar_label()

    def agregar_label(self):
        if self.tipo != BOTON_TIPO_VOLUMEN:
            max_width, max_height = self.imagen.get_size()
            fuente = pygame.font.Font(FUENTE_PATH, 15)
            text = fuente.render(self.label, True, (255, 255, 255))
            self.imagen.blit(text, (max_width // 2 - text.get_width() // 2, max_height // 2 - text.get_height() // 2))

    def disparar_efecto_hover(self):
        self.imagen = self.imagen_original.copy()
        brillo = pygame.Surface(self.imagen.get_size(), pygame.SRCALPHA)
        brillo.fill((30, 30, 30, 0))
        self.imagen.blit(brillo, (0, 0), special_flags=pygame.BLEND_RGB_ADD)
        self.agregar_label()

    def remover_efecto_hover(self):
        self.imagen = self.imagen_original.copy()
        self.agregar_label()

    def obtener_rectangulo(self, contenedor: pygame.Surface, posicion_contenedor: Coordenada = None):
        boton_x = calcular_centro_horizontal(contenedor, self.imagen)
        boton_y = self.posicion.y + 50

        if posicion_contenedor:
            boton_x += posicion_contenedor.x
            boton_y += posicion_contenedor.y

        boton_width, boton_height = self.imagen.get_size()
        boton_rect = pygame.Rect(boton_x, boton_y, boton_width, boton_height)

        return boton_rect