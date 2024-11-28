import pygame
import pygame.locals
from Funciones import *
from Constantes import *

pygame.init()

#funcion que mescla las pregunta
lista_preguntas = leer_csv("preguntas.csv")

#cargar boton para preguntas
boton_preguntas = pygame.image.load("assets/boton_pregunta.png")


#crear botones

botones = crear_botones(boton_preguntas,350,70,4)

boton_pregunta = crear_botones(boton_preguntas,400,300,1)


#importar sonido error y acierto
pygame.mixer.init()
error = pygame.mixer.Sound("assets/error_sound.mp3")
correcto = pygame.mixer.Sound("assets/sound_correcto.mp3")



#cargo fondo para juego
fondo_juego = pygame.image.load("assets/fondo_juego.jpeg")
#redimensionado del fondo
fondo_juego= pygame.transform.scale(fondo_juego, VENTANA)


sortear_lista(lista_preguntas)

mi_fuente = pygame.font.SysFont("Verdana",25)




#creamos el evento tiempo
evento_tiempo_1s = pygame.USEREVENT
pygame.time.set_timer(evento_tiempo_1s,1000)

#contador de tiempo



def abrir_juego(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event], juego)-> str:

    if juego["vidas"] < 1:
        retorno = "fin_partida"
    else:
        retorno = "Juego"
    #print(lista_preguntas[0])
    for evento in cola_eventos:
        #print(lista_preguntas[0])

        if evento.type == pygame.QUIT:
            retorno = "Salir"
        if evento.type == evento_tiempo_1s:
            juego["tiempo"] -= 1
            if juego["tiempo"] <= 0:
                retorno = "fin_partida" 

        if evento.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()

            #detectar colisiones y apartir de ahi evaluar que boon se presiona y tambien si la respeusta es correcta o incorrecta
            if botones[0]["rectangulo"].collidepoint(pos):

                juego["tiempo"] = gestionar_puntuacion(lista_preguntas,juego,1,juego["tiempo"],error, correcto)

            elif botones[1]["rectangulo"].collidepoint(pos):
                
                juego["tiempo"] = gestionar_puntuacion(lista_preguntas,juego,2,juego["tiempo"],error, correcto)
                
            elif botones[2]["rectangulo"].collidepoint(pos):
                
                juego["tiempo"] = gestionar_puntuacion(lista_preguntas,juego,3,juego["tiempo"],error, correcto)
                
            elif botones[3]["rectangulo"].collidepoint(pos):
                juego["tiempo"] = gestionar_puntuacion(lista_preguntas,juego,4,juego["tiempo"],error, correcto)


    texto = mi_fuente.render(f"SEGUNDOS: {juego["tiempo"]}",False,COLOR_ROJO)
    
    #posicionamiento de botones
    posicionar_botones(centro_pantalla_ancho,centro_pantalla_alto, botones[0]["rectangulo"])

    posicionar_botones(centro_pantalla_ancho,centro_pantalla_alto+70, botones[1]["rectangulo"])

    posicionar_botones(centro_pantalla_ancho,centro_pantalla_alto+140, botones[2]["rectangulo"])

    posicionar_botones(centro_pantalla_ancho,centro_pantalla_alto+210, botones[3]["rectangulo"])

    posicionar_botones(centro_pantalla_ancho,centro_pantalla_alto-200, boton_pregunta[0]["rectangulo"])

    
    
    pantalla.fill(COLOR_BLANCO)

    

    #dibuja los botones en pantalla
    pantalla.blit(fondo_juego, (0,0))
    pantalla.blit(botones[0]["superficie"],(botones[0]["rectangulo"].x, botones[0]["rectangulo"].y))
    pantalla.blit(botones[1]["superficie"],(botones[1]["rectangulo"].x, botones[1]["rectangulo"].y))
    pantalla.blit(botones[2]["superficie"],(botones[2]["rectangulo"].x, botones[2]["rectangulo"].y))
    pantalla.blit(botones[3]["superficie"],(botones[3]["rectangulo"].x, botones[3]["rectangulo"].y))
    pantalla.blit(boton_pregunta[0]["superficie"],(boton_pregunta[0]["rectangulo"].x, boton_pregunta[0]["rectangulo"].y))
    mostrar_respuestas(pantalla,lista_preguntas,botones,mi_fuente)
    mostrar_texto(pantalla,f"vidas: {juego["vidas"]}",(10,20),mi_fuente,COLOR_ROJO)
    mostrar_texto(pantalla,f"puntuacion: {juego["puntuacion"]}",(10,50),mi_fuente,COLOR_ROJO)

    #las preguntas se superponen y el texto se renderiza con simbolos
    mostrar_texto(boton_pregunta[0]["superficie"],lista_preguntas[0]["pregunta"],(boton_pregunta[0]["rectangulo"].centerx-350, boton_pregunta[0]["rectangulo"].centery-100),mi_fuente,COLOR_AZUL, line_spacing=10, align='left')
    pantalla.blit(texto,(10,120))
    

    
    return retorno