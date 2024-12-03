import pygame
import time

def calcular_centro_horizontal(contenedor: pygame.Surface, elemento: pygame.Surface) -> int:
    return contenedor.get_width() // 2 - elemento.get_width() // 2

def calcular_centro_vertical(contenedor: pygame.Surface, elemento: pygame.Surface) -> int:
    return contenedor.get_height() // 2 - elemento.get_height() // 2

def obtener_fecha():
    timestamp = time.time()
    tiempo_local = time.localtime(timestamp)
    fecha_legible = time.strftime("%d/%m/%Y", tiempo_local)
    return fecha_legible

def reproducir_sonido(sonido):
    sonido.play()
