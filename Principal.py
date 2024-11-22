import pygame
from Menu import *
from Juego import *

pygame.init()

screen = pygame.display.set_mode(VENTANA)

icono = pygame.image.load("assets/icono.png")
pygame.display.set_icon(icono)

clock = pygame.time.Clock()

corriendo = True

ventana_actual = "Menu"

puntos = 0

while corriendo:

    eventos = pygame.event.get()    

    if ventana_actual == "Menu":
        ventana_actual = abrir_menu_juego(screen, eventos)
    elif ventana_actual == "Juego":
        ventana_actual = abrir_juego(screen,eventos)
    elif ventana_actual == "Salir":
        corriendo = False


    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()