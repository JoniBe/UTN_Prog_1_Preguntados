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

#boton imagen
boton_img = pygame.image.load("assets/play_boton.jpg")
boton_rectangulo = boton_img.get_rect()

icono = pygame.image.load("assets/icono.png")

pygame.display.set_icon(icono)
clock = pygame.time.Clock()

#funcion que mescla las pregunta
lista_preguntas = leer_csv("preguntas.csv")


run_menu = True
run = True

#menu

def abrir_menu():
    global run_menu
    global run

    while run_menu:
        boton_rectangulo.centerx = ANCHO/2
        boton_rectangulo.centery = ALTO/2 
        for evento in pygame.event.get():
            #cerrar juego estableciendo las 2 variables en false
            if evento.type == pygame.QUIT:
                run = False
                run_menu = False
            if evento.type == pygame.MOUSEBUTTONDOWN:
                  pos = pygame.mouse.get_pos()
                  if boton_rectangulo.collidepoint(pos):
                      print("el juego empezo")
                      run_menu = False
    

        

        
        pantalla.blit(fondo_menu, (0,0))
        pantalla.blit(boton_img,(boton_rectangulo.x, boton_rectangulo.y))


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
