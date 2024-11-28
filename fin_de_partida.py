import pygame
from Constantes import *
from Funciones import *


fondo_fin = pygame.image.load("assets/fondo_din.jpeg")

fondo_fin_resize = pygame.transform.scale(fondo_fin, VENTANA)

campo_nombre = pygame.image.load("assets/boton_pregunta.png")

campo = crear_botones(campo_nombre,500,70,1)
aceptar = crear_botones(campo_nombre,300,70,1)


fuente = pygame.font.SysFont("Verdana",30)

nombre = ""

bandera_camnpo1 = False

def terminar_juego(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event],juego)-> str:
    global bandera_camnpo1
    global nombre
    retorno = "fin_partida"
    #print(lista_preguntas[0])
    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = "Salir"
        if evento.type == pygame.MOUSEBUTTONDOWN:
            bandera_camnpo1 = activar_campo(campo, bandera_camnpo1)

        if evento.type == pygame.KEYDOWN:

            if bandera_camnpo1 == True:
                #letra_presionada = chr(evento.key)
                letra_presionada = str(evento.unicode)


            
                if evento.key == pygame.K_BACKSPACE:  # Si se presiona Backspace
                    # Eliminar el último carácter del nombre
                    nombre = nombre[:-1]
                elif letra_presionada and len(nombre) < 20 and not(evento.key == pygame.K_BACKSPACE):
                    letra_presionada
                    nombre += letra_presionada
        if evento.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if aceptar[0]["rectangulo"].collidepoint(pos):
                
                #guardamos datos en json
                lista_puntuacion = []
                informacion = {}
                informacion["puntos"] = juego["puntuacion"]
                informacion["fecha"] = obtener_fecha()
                informacion["nombre"] = nombre
                lista_puntuacion.append(informacion)
                generar_json("puntos.json", lista_puntuacion)

                #restablecemos las variables
                restablecer_variables(juego)

                nombre = ""
                retorno = "Menu"
            
        


    texto_renderizado = fuente.render(nombre, True, COLOR_ROJO)
    aceptar_renderizado = fuente.render("Aceptar", True, COLOR_ROJO)        

    posicionar_botones(centro_pantalla_ancho,centro_pantalla_alto, campo[0]["rectangulo"])
    posicionar_botones(centro_pantalla_ancho,centro_pantalla_alto+100, aceptar[0]["rectangulo"])

    

    pantalla.blit(fondo_fin_resize,(0,0))
    pantalla.blit(campo[0]["superficie"],(campo[0]["rectangulo"].x, campo[0]["rectangulo"].y))
    pantalla.blit(aceptar[0]["superficie"],(aceptar[0]["rectangulo"].x, aceptar[0]["rectangulo"].y))

    pantalla.blit(texto_renderizado,(campo[0]["rectangulo"].centerx-170, campo[0]["rectangulo"].centery-20))
    pantalla.blit(aceptar_renderizado,(aceptar[0]["rectangulo"].centerx-60, aceptar[0]["rectangulo"].centery-20))
    
    

    
    return retorno