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

#sonido de explosion
bomba_sound= pygame.mixer.Sound("assets/explosion.mp3")


#cargo cmomodin bomba 
bomba_img = pygame.image.load("assets/bomba_comodin_boton_nofondo.png")
x2_img = pygame.image.load("assets/x2_sinfondo.png")
chance_img = pygame.image.load("assets/doble_chance.png")
pasar_img = pygame.image.load("assets/pasar.png")

#creo los botones para comodines

boton_bomba = crear_botones(bomba_img,80,100,1)
boton_x2 = crear_botones(x2_img,80,80,1)
boton_chance = crear_botones(chance_img,80,80,1)
boton_pasar = crear_botones(pasar_img,80,80,1)


sortear_lista(lista_preguntas)

mi_fuente = pygame.font.SysFont("Verdana",25)




#creamos el evento tiempo
evento_tiempo_1s = pygame.USEREVENT
pygame.time.set_timer(evento_tiempo_1s,1000)


#banderas aparecer o desaparecer boton
desaparecer_btn = {"btn_respuesta1": False, "btn_respuesta2": False,"btn_respuesta3": False,"btn_respuesta4": False}


#banderas comodines
bomba_explotada = False
bandera_x2 = False
comodin_pasar = False
comodin_chance_bandera = False




def abrir_juego(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event], juego)-> str:
    global bomba_explotada
    global bandera_x2
    global comodin_pasar
    global comodin_chance_bandera
    botones_lista_touch = {"btn1": False, "btn2": False,"btn3": False,"btn4": False}

    if juego["vidas"] < 1:
        pygame.mixer.music.stop()
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

            #detectar colisiones y apartir de ahi evaluar que boon se presiona y tambien si la respeusta es correcta o incorrecta, tambien si se presiona un comodin
            if botones[0]["rectangulo"].collidepoint(pos):
                

                juego["tiempo"] = gestionar_puntuacion(lista_preguntas,juego,1,juego["tiempo"],error, correcto, desaparecer_btn,bandera_x2)
                bomba_explotada = False
                bandera_x2 = False
                comodin_pasar = False
                comodin_chance_bandera = False
                botones_lista_touch["btn1"] = True
                comodin_doble_chance(comodin_chance_bandera,lista_preguntas,botones_lista_touch,desaparecer_btn,1)

            elif botones[1]["rectangulo"].collidepoint(pos):
                
                juego["tiempo"] = gestionar_puntuacion(lista_preguntas,juego,2,juego["tiempo"],error, correcto, desaparecer_btn,bandera_x2)
                bomba_explotada = False
                bandera_x2 = False
                comodin_pasar = False
                comodin_chance_bandera = False
                botones_lista_touch["btn2"] = True
                comodin_doble_chance(comodin_chance_bandera,lista_preguntas,botones_lista_touch,desaparecer_btn,2)

            elif botones[2]["rectangulo"].collidepoint(pos):
                
                juego["tiempo"] = gestionar_puntuacion(lista_preguntas,juego,3,juego["tiempo"],error, correcto, desaparecer_btn,bandera_x2)
                bomba_explotada = False
                bandera_x2 = False
                comodin_pasar = False
                comodin_chance_bandera = False
                botones_lista_touch["btn3"] = True
                comodin_doble_chance(comodin_chance_bandera,lista_preguntas,botones_lista_touch,desaparecer_btn,3)

                
            elif botones[3]["rectangulo"].collidepoint(pos):
                juego["tiempo"] = gestionar_puntuacion(lista_preguntas,juego,4,juego["tiempo"],error, correcto, desaparecer_btn,bandera_x2)
                bomba_explotada = False
                bandera_x2 = False
                comodin_pasar = False
                comodin_chance_bandera = False
                botones_lista_touch["btn4"] = True
                comodin_doble_chance(comodin_chance_bandera,lista_preguntas,botones_lista_touch,desaparecer_btn,4)


            

            #detectar comodines---------------------------------------

            elif boton_bomba[0]["rectangulo"].collidepoint(pos) and juego["bomba"] > 0 and bomba_explotada == False:

                bomba_explotada = controlar_comodin_bomba(bomba_sound,lista_preguntas,desaparecer_btn,juego, bomba_explotada)

            elif boton_x2[0]["rectangulo"].collidepoint(pos):
                if juego["x2"] > 0 and bandera_x2 == False:
                    bandera_x2 = True
                    juego["x2"] -= 1

            elif boton_chance[0]["rectangulo"].collidepoint(pos):
                if juego["pasar"] > 0 and comodin_chance_bandera == False:
                    comodin_chance_bandera = True
                    juego["doble_chance"] -= 1

            elif boton_pasar[0]["rectangulo"].collidepoint(pos):
                
                if juego["pasar"] > 0 and comodin_pasar == False:
                    comodin_pasar = True
                    juego["pasar"] -= 1
                    sortear_lista(lista_preguntas)
                    



    texto = mi_fuente.render(f"SEGUNDOS: {juego["tiempo"]}",False,COLOR_ROJO)
    cantidad_bombas = mi_fuente.render(f"{juego["bomba"]}x",False,COLOR_ROJO)
    cantidad_x2 = mi_fuente.render(f"{juego["x2"]}x",False,COLOR_ROJO)
    cantidad_pasar = mi_fuente.render(f"{juego["pasar"]}x",False,COLOR_ROJO)
    cantidad_chance = mi_fuente.render(f"{juego["doble_chance"]}x",False,COLOR_ROJO)



    #posicionamiento de botones y tambien lo podemos hacer desaparecer por medio de la bandera
    if desaparecer_btn["btn_respuesta1"] == True:
        posicionar_botones(centro_pantalla_ancho,centro_pantalla_alto+2000, botones[0]["rectangulo"])
    else:
        posicionar_botones(centro_pantalla_ancho,centro_pantalla_alto, botones[0]["rectangulo"])

    if desaparecer_btn["btn_respuesta2"] == True:
        posicionar_botones(centro_pantalla_ancho,centro_pantalla_alto+2000, botones[1]["rectangulo"])
    else:
        posicionar_botones(centro_pantalla_ancho,centro_pantalla_alto+70, botones[1]["rectangulo"])

    if desaparecer_btn["btn_respuesta3"] == True:
        posicionar_botones(centro_pantalla_ancho,centro_pantalla_alto+2000, botones[2]["rectangulo"])
    else:
        posicionar_botones(centro_pantalla_ancho,centro_pantalla_alto+140, botones[2]["rectangulo"])

    if desaparecer_btn["btn_respuesta4"] == True:
        posicionar_botones(centro_pantalla_ancho,centro_pantalla_alto+2000, botones[3]["rectangulo"])
    else:
        posicionar_botones(centro_pantalla_ancho,centro_pantalla_alto+210, botones[3]["rectangulo"])

    #se posiciona el campo donde se escribe la pregunta
    posicionar_botones(centro_pantalla_ancho,centro_pantalla_alto-200, boton_pregunta[0]["rectangulo"])


    #se pocisionan los comodines
    posicionar_botones(centro_pantalla_ancho+350,centro_pantalla_alto-40, boton_bomba[0]["rectangulo"])

    posicionar_botones(centro_pantalla_ancho+350,centro_pantalla_alto+50, boton_x2[0]["rectangulo"])

    posicionar_botones(centro_pantalla_ancho+350,centro_pantalla_alto+150, boton_chance[0]["rectangulo"])

    posicionar_botones(centro_pantalla_ancho+350,centro_pantalla_alto+250, boton_pasar[0]["rectangulo"])

    
    
    pantalla.fill(COLOR_BLANCO)

    

    #dibuja los botones en pantalla
    pantalla.blit(fondo_juego, (0,0))
    pantalla.blit(botones[0]["superficie"],(botones[0]["rectangulo"].x, botones[0]["rectangulo"].y))
    pantalla.blit(botones[1]["superficie"],(botones[1]["rectangulo"].x, botones[1]["rectangulo"].y))
    pantalla.blit(botones[2]["superficie"],(botones[2]["rectangulo"].x, botones[2]["rectangulo"].y))
    pantalla.blit(botones[3]["superficie"],(botones[3]["rectangulo"].x, botones[3]["rectangulo"].y))

    #dibujamos comodines
    pantalla.blit(boton_bomba[0]["superficie"],(boton_bomba[0]["rectangulo"].x,boton_bomba[0]["rectangulo"].y))
    pantalla.blit(boton_x2[0]["superficie"],(boton_x2[0]["rectangulo"].x,boton_x2[0]["rectangulo"].y))

    pantalla.blit(boton_chance[0]["superficie"],(boton_chance[0]["rectangulo"].x,boton_chance[0]["rectangulo"].y))
    pantalla.blit(boton_pasar[0]["superficie"],(boton_pasar[0]["rectangulo"].x,boton_pasar[0]["rectangulo"].y))
    #---------------

    pantalla.blit(boton_pregunta[0]["superficie"],(boton_pregunta[0]["rectangulo"].x, boton_pregunta[0]["rectangulo"].y))
    mostrar_respuestas(pantalla,lista_preguntas,botones,mi_fuente)
    mostrar_texto(pantalla,f"vidas: {juego["vidas"]}",(10,20),mi_fuente,COLOR_ROJO)
    mostrar_texto(pantalla,f"puntuacion: {juego["puntuacion"]}",(10,50),mi_fuente,COLOR_ROJO)

    #las preguntas se superponen y el texto se renderiza con simbolos
    mostrar_texto(boton_pregunta[0]["superficie"],lista_preguntas[0]["pregunta"],(boton_pregunta[0]["rectangulo"].centerx-350, boton_pregunta[0]["rectangulo"].centery-100),mi_fuente,COLOR_AZUL, line_spacing=10, align='left')
    pantalla.blit(texto,(10,120))
    pantalla.blit(cantidad_bombas,(boton_bomba[0]["rectangulo"].x-50,boton_bomba[0]["rectangulo"].centery-15))
    pantalla.blit(cantidad_x2,(boton_x2[0]["rectangulo"].x-50,boton_x2[0]["rectangulo"].centery-15))
    pantalla.blit(cantidad_pasar,(boton_pasar[0]["rectangulo"].x-50,boton_pasar[0]["rectangulo"].centery-15))
    pantalla.blit(cantidad_chance,(boton_chance[0]["rectangulo"].x-50,boton_chance[0]["rectangulo"].centery-15))
    

    
    return retorno