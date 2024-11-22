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

#crear botones

botones = crear_botones(boton_preguntas,300,70,4)


#ejes del centro de pantalla
centro_pantalla_ancho = ANCHO/2
centro_pantalla_alto = ALTO/2




sortear_lista(lista_preguntas)




def abrir_juego(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event], juego)-> str:
    retorno = "Juego"
    #print(lista_preguntas[0])
    for evento in cola_eventos:

        if evento.type == pygame.QUIT:
            retorno = "Salir"
        if evento.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()

            if botones[0]["rectangulo"].collidepoint(pos):
                if lista_preguntas[0]["correcta"] == str(1):

                    print("Correcto")
                    juego["puntuacion"] += PUNTUACION_ACIERTO
                else:
                    print("incorrecto")
            elif botones[1]["rectangulo"].collidepoint(pos):
                
                if lista_preguntas[0]["correcta"] == str(2):

                    print("Correcto")
                    juego["puntuacion"] += PUNTUACION_ACIERTO
                else:
                    print("incorrecto")

            elif botones[2]["rectangulo"].collidepoint(pos):
                
                if lista_preguntas[0]["correcta"] == str(3):

                    print("Correcto")
                    juego["puntuacion"] += PUNTUACION_ACIERTO
                else:
                    print("incorrecto")
            elif botones[3]["rectangulo"].collidepoint(pos):
                if lista_preguntas[0]["correcta"] == str(4):

                    print("Correcto")
                    juego["puntuacion"] += PUNTUACION_ACIERTO
                else:
                    print("incorrecto")


    
    #posicionamiento de botones
    posicionar_botones(centro_pantalla_ancho,centro_pantalla_alto, botones[0]["rectangulo"])

    posicionar_botones(centro_pantalla_ancho,centro_pantalla_alto+70, botones[1]["rectangulo"])

    posicionar_botones(centro_pantalla_ancho,centro_pantalla_alto+140, botones[2]["rectangulo"])

    posicionar_botones(centro_pantalla_ancho,centro_pantalla_alto+210, botones[3]["rectangulo"])

    
    
    pantalla.fill(COLOR_BLANCO)

    #dibuja los botones en pantalla

    pantalla.blit(botones[0]["superficie"],(botones[0]["rectangulo"].x, botones[0]["rectangulo"].y))
    pantalla.blit(botones[1]["superficie"],(botones[1]["rectangulo"].x, botones[1]["rectangulo"].y))
    pantalla.blit(botones[2]["superficie"],(botones[2]["rectangulo"].x, botones[2]["rectangulo"].y))
    pantalla.blit(botones[3]["superficie"],(botones[3]["rectangulo"].x, botones[3]["rectangulo"].y))
    
    

    
    return retorno