import pygame
from Funciones import *
from Constantes import *

pygame.init()

#funcion que mescla las pregunta
lista_preguntas = leer_csv("preguntas.csv")

#cargar boton para preguntas
boton_preguntas = pygame.image.load("assets/boton_pregunta.png")

#establecer fuente y tamaño
arial = pygame.font.SysFont("Arial Narrow",25)

#aca se escala la imagen del boton y se le crea un rectangulo o hitbox

boton_preguntas_size = pygame.transform.scale(boton_preguntas, (500,70))
boton_preguntas_rectangulo = boton_preguntas_size.get_rect()


boton_preguntas_size1 = pygame.transform.scale(boton_preguntas, (500,70))
boton_preguntas_rectangulo1 = boton_preguntas_size.get_rect()

boton_preguntas_size2 = pygame.transform.scale(boton_preguntas, (500,70))
boton_preguntas_rectangulo2 = boton_preguntas_size.get_rect()

boton_preguntas_size3 = pygame.transform.scale(boton_preguntas, (500,70))
boton_preguntas_rectangulo3 = boton_preguntas_size.get_rect()


boton_preguntas_size4 = pygame.transform.scale(boton_preguntas, (500,70))
boton_preguntas_rectangulo4 = boton_preguntas_size.get_rect()

#ejes del centro de pantalla
centro_pantalla_ancho = ANCHO/2
centro_pantalla_alto = ALTO/2








def abrir_juego(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event])-> str:
    retorno = "Juego"

    for evento in cola_eventos:

        if evento.type == pygame.QUIT:
            retorno = "Salir"
        if evento.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()

            if boton_preguntas_rectangulo.collidepoint(pos):
                print("tocaste boton 1")
                #sortea preguntas
                sortear_lista(lista_preguntas)
            elif boton_preguntas_rectangulo1.collidepoint(pos):
                print("tocaste boton 2")
            elif boton_preguntas_rectangulo2.collidepoint(pos):
                print("tocaste boton 3")
            elif boton_preguntas_rectangulo3.collidepoint(pos):
                print("tocaste boton 4")

    
    #posicionamiento de botones

    boton_preguntas_rectangulo.centerx = centro_pantalla_ancho
    boton_preguntas_rectangulo.centery = centro_pantalla_alto

    boton_preguntas_rectangulo1.centerx = centro_pantalla_ancho
    boton_preguntas_rectangulo1.centery = centro_pantalla_alto + 70

    boton_preguntas_rectangulo2.centerx = centro_pantalla_ancho
    boton_preguntas_rectangulo2.centery = centro_pantalla_alto + 140

    boton_preguntas_rectangulo3.centerx = centro_pantalla_ancho
    boton_preguntas_rectangulo3.centery = centro_pantalla_alto + 210
    
    pantalla.fill(COLOR_BLANCO)

    #dibuja los botones en pantalla

    pantalla.blit(boton_preguntas_size,(boton_preguntas_rectangulo.x, boton_preguntas_rectangulo.y))
    pantalla.blit(boton_preguntas_size1,(boton_preguntas_rectangulo1.x, boton_preguntas_rectangulo1.y))
    pantalla.blit(boton_preguntas_size2,(boton_preguntas_rectangulo2.x, boton_preguntas_rectangulo2.y))
    pantalla.blit(boton_preguntas_size3,(boton_preguntas_rectangulo3.x, boton_preguntas_rectangulo3.y))
    

    
    return retorno