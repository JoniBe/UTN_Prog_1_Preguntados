import pygame
from Constantes import *
from Funciones import *

pygame.init()

#se establece ancho y alto de la pantalla
pantalla = pygame.display.set_mode(VENTANA_MEDIDA)

#se carga imagen del fondo del menu

fondo_menu = pygame.image.load("assets/fondo_menu.jpeg")
#redimensionado del fondo
fondo_menu = pygame.transform.scale(fondo_menu, VENTANA_MEDIDA)

#boton imagen
boton_img = pygame.image.load("assets/play_boton.jpg")
boton_rectangulo = boton_img.get_rect()

#cargamos musica
pygame.mixer.init()
pygame.mixer.music.load("assets/cancion_juego.mp3")

def abrir_menu_juego(pantalla:pygame.surface,cola_eventos:list[pygame.event.Event],juego)-> str:
    retorno = "Menu"

    boton_rectangulo.centerx = VENTANA_WIDTH // 2
    boton_rectangulo.centery = VENTANA_HEIGHT //2 

    for evento in cola_eventos:
        #cerrar juego estableciendo las 2 variables en false
        if evento.type == pygame.QUIT:
            retorno = "Salir"
        if evento.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if boton_rectangulo.collidepoint(pos):
                pygame.mixer.music.play(-1)
                juego["tiempo"] = 30
                retorno = "Juego"
    

        
        
    pantalla.blit(fondo_menu, (0,0))
    pantalla.blit(boton_img,(boton_rectangulo.x, boton_rectangulo.y))
    return retorno

