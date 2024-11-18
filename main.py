import pygame
from Constantes import *
from Funciones import *

pygame.init()
pantalla = pygame.display.set_mode(VENTANA)
icono = pygame.image.load("icono.png")
pygame.display.set_icon(icono)
clock = pygame.time.Clock()


run = True

while run:

    for evento in pygame.event.get():
        #cerrar juego
        if evento.type == pygame.QUIT:
            run = False
    


    

    pantalla.fill(COLOR_BLANCO)



    #actualziacion de pantalla
    pygame.display.flip()

    #FPS
    clock.tick(FPS)


pygame.quit()
