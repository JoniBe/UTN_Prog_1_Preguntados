import pygame
from Constantes import *
from Funciones import *

pygame.init()
pantalla = pygame.display.set_mode(VENTANA)
icono = pygame.image.load("icono.png")
pygame.display.set_icon(icono)
clock = pygame.time.Clock()

lista_preguntas = leer_csv("preguntas.csv")

run = True

while run:

    for evento in pygame.event.get():
        #cerrar juego
        if evento.type == pygame.QUIT:
            run = False
        if evento.type == pygame.MOUSEBUTTONDOWN:
            print(lista_preguntas[4])
    

    #detectar pulso constante de taclas
    teclas = pygame.key.get_pressed()

    if teclas[pygame.K_3]:
        print("se toco la tecla 3")


    

    pantalla.fill(COLOR_BLANCO)



    #actualziacion de pantalla
    pygame.display.flip()

    #FPS
    clock.tick(FPS)


pygame.quit()
