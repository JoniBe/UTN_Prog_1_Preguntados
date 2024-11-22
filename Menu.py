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




def abrir_menu_juego(pantalla:pygame.surface,cola_eventos:list[pygame.event.Event])-> str:
    retorno = "Menu"

    boton_rectangulo.centerx = ANCHO/2
    boton_rectangulo.centery = ALTO/2 

    for evento in cola_eventos:
        #cerrar juego estableciendo las 2 variables en false
        if evento.type == pygame.QUIT:
            retorno = "Salir"
        if evento.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if boton_rectangulo.collidepoint(pos):
                print("el juego empezo")
                retorno = "Juego"
    

        

        
    pantalla.blit(fondo_menu, (0,0))
    pantalla.blit(boton_img,(boton_rectangulo.x, boton_rectangulo.y))
    return retorno

