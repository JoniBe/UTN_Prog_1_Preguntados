import pygame
from Constantes import *
from Funciones import *

pygame.init()

#se establece ancho y alto de la pantalla
pantalla = pygame.display.set_mode(VENTANA)

#se carga imagen del fondo del menu

fondo_menu = pygame.image.load("assets/fondo_menu.jpeg")
#redimensionado del fondo
fondo_menu = pygame.transform.scale(fondo_menu, VENTANA)

icono = pygame.image.load("assets/icono.png")
pygame.display.set_icon(icono)
clock = pygame.time.Clock()

lista_preguntas = leer_csv("preguntas.csv")


run_menu = True
run = True

#menu

def abrir_menu():
    global run_menu
    global run

    while run_menu:

        for evento in pygame.event.get():
            #cerrar juego estableciendo las 2 variables en false
            if evento.type == pygame.QUIT:
                run = False
                run_menu = False
    

        pantalla.blit(fondo_menu, (0,0))



        #actualziacion de pantalla
        pygame.display.flip()

        #FPS
        clock.tick(FPS)

#iniciar menu
abrir_menu()

#iniciar juego
while run:

    for evento in pygame.event.get():
        #cerrar juego
        if evento.type == pygame.QUIT:
            run = False
            run_menu = False

    

    pantalla.fill(COLOR_BLANCO)



    #actualziacion de pantalla
    pygame.display.flip()

    #FPS
    clock.tick(FPS)


pygame.quit()
