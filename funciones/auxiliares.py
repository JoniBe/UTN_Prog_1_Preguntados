import pygame

def calcular_centro_horizontal(contenedor: pygame.Surface, elemento: pygame.Surface) -> int:
    return contenedor.get_width() // 2 - elemento.get_width() // 2

def calcular_centro_vertical(contenedor: pygame.Surface, elemento: pygame.Surface) -> int:
    return contenedor.get_height() // 2 - elemento.get_height() // 2
