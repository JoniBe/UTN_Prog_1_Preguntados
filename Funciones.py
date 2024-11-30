import random
import pygame
from constantes import *
import json
import time
from modelos.pregunta import Pregunta

def leer_csv(archivo:str)-> list:

    lista = []

    with open(archivo) as file:

        for line in file.readlines():
            pregunta = line.split(",")
            diccionario = {"pregunta": pregunta[0].replace("Â",""), "respuesta_1" : pregunta[1], "respuesta_2" : pregunta[2], "respuesta_3" : pregunta[3], "respuesta_4" : pregunta[4], "correcta" : pregunta[5].replace("\n", "")}
            lista.append(diccionario)
    return lista

def sortear_lista(lista:list) -> list:
    lista_sorteada = random.shuffle(lista)
    return lista_sorteada


def crear_botones(imagen,ancho,alto,cantidad)->list:

    lista_botones = []

    for i in range(cantidad):
        boton_superficie = pygame.transform.scale(imagen, (ancho,alto)) 
        boton_rectangulo = boton_superficie.get_rect()
        diccionario = {"superficie": boton_superficie, "rectangulo" : boton_rectangulo}
        lista_botones.append(diccionario)
    
    return lista_botones

def posicionar_botones(posx,posy, objeto):
    objeto.centery = posy
    objeto.centerx = posx



def mostrar_texto(surface, text, pos, font, color=pygame.Color('black'), line_spacing=5, align='left'):
    words = text.split(' ')  # Dividimos el texto en palabras
    space_width = font.size(' ')[0]  # El ancho de un espacio
    max_width, max_height = surface.get_size()
    
    # Posición inicial
    x, y = pos
    current_line = []
    current_line_width = 0

    # Calcular alineación
    if align == 'center':
        x = (max_width - font.size(text)[0]) // 2  # Centra el texto

    for word in words:
        word_surface = font.render(word, False, color)
        word_width, word_height = word_surface.get_size()

        # Si añadir la palabra excede el ancho de la pantalla, cambiamos a la siguiente línea
        if current_line_width + word_width + (len(current_line) - 1) * space_width > max_width:
            # Dibujamos la línea anterior
            for i, w in enumerate(current_line):
                word_surface = font.render(w, False, color)
                word_width, word_height = word_surface.get_size()
                surface.blit(word_surface, (x + sum(font.size(w)[0] + space_width for w in current_line[:i]), y))
            y += word_height + line_spacing  # Ajusta el espacio entre líneas
            current_line = [word]
            current_line_width = word_width
        else:
            current_line.append(word)
            current_line_width += word_width + space_width
    
    # Dibujar la última línea
    for i, w in enumerate(current_line):
        word_surface = font.render(w, False, color)
        word_width, word_height = word_surface.get_size()
        surface.blit(word_surface, (x + sum(font.size(w)[0] + space_width for w in current_line[:i]), y))


def gestionar_puntuacion(lista_preguntas, juego,btn, cantidad_segundos,sonido_error,sonido_acierto,posicion_btn, bandera_x2,comodin_chance_bandera,botones_lista_touch,desaparecer_btn):

    posicion_btn["btn_respuesta1"] = False
    posicion_btn["btn_respuesta2"] = False
    posicion_btn["btn_respuesta3"] = False
    posicion_btn["btn_respuesta4"] = False

    if lista_preguntas[0]["correcta"] == str(btn):
        
        if bandera_x2 == True:
            reproducir_sonido(sonido_acierto)
            print(f"Correcto{juego["acertados_seguidos"]}")
            juego["puntuacion"] += PUNTUACION_ACIERTO * 2
            juego["acertados_seguidos"] += 1

            if juego["acertados_seguidos"] == 5:
                juego["vidas"] += 1
                cantidad_segundos += 20

            if juego["acertados_seguidos"] > 4:
                juego["acertados_seguidos"] = 0
        else:
            reproducir_sonido(sonido_acierto)
            print(f"Correcto{juego["acertados_seguidos"]}")
            juego["puntuacion"] += PUNTUACION_ACIERTO
            juego["acertados_seguidos"] += 1

            if juego["acertados_seguidos"] == 5:
                juego["vidas"] += 1
                cantidad_segundos += 20

            if juego["acertados_seguidos"] > 4:
                juego["acertados_seguidos"] = 0

        

        sortear_lista(lista_preguntas)
    else:
        #comprueba bandera para saber si activar comodin chance o no
        if comodin_chance_bandera == True:                          
            #con esto se que boon estoy tocando para hacerlo desaparecer
            if botones_lista_touch["btn1"] == True:
                desaparecer_btn["btn_respuesta1"] = True
            elif botones_lista_touch["btn2"] == True:
                desaparecer_btn["btn_respuesta2"] = True
            elif botones_lista_touch["btn3"] == True:
                desaparecer_btn["btn_respuesta3"] = True
            elif botones_lista_touch["btn4"] == True:
                desaparecer_btn["btn_respuesta4"] = True
        else:
            reproducir_sonido(sonido_error)
            juego["puntuacion"] += PUNTUACION_ERROR
            juego["vidas"] -= 1
            juego["acertados_seguidos"] = 0
            sortear_lista(lista_preguntas)
    return cantidad_segundos


def mostrar_respuestas(pantalla,lista_preguntas, botones, mi_fuente):

    mostrar_texto(pantalla,lista_preguntas[0]["respuesta_1"],(botones[0]["rectangulo"].centerx-120, botones[0]["rectangulo"].centery-10),mi_fuente,COLOR_AZUL)
    mostrar_texto(pantalla,lista_preguntas[0]["respuesta_2"],(botones[1]["rectangulo"].centerx-120, botones[1]["rectangulo"].centery-10),mi_fuente,COLOR_AZUL)
    mostrar_texto(pantalla,lista_preguntas[0]["respuesta_3"],(botones[2]["rectangulo"].centerx-120, botones[2]["rectangulo"].centery-10),mi_fuente,COLOR_AZUL)
    mostrar_texto(pantalla,lista_preguntas[0]["respuesta_4"],(botones[3]["rectangulo"].centerx-120, botones[3]["rectangulo"].centery-10),mi_fuente,COLOR_AZUL)

def activar_campo(campo,bandera):

    retorno = False
    pos = pygame.mouse.get_pos()
    if campo[0]["rectangulo"].collidepoint(pos):
        retorno = True
    return retorno

def generar_json(nombre_archivo:str, lista:list, nombre:str) -> bool: 
    if len(nombre) > 0:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            contenido = json.load(archivo)
        contenido.extend(lista)    
    
        with open(nombre_archivo,'w') as archivo:
            json.dump(contenido, archivo, indent=4)

def obtener_fecha():
    # Obtener la hora actual en formato timestamp (segundos desde la época)
    timestamp = time.time()
    
    # Convertir el timestamp en una estructura de tiempo local
    tiempo_local = time.localtime(timestamp)
    
    # Convertir la estructura de tiempo local a una cadena de texto en formato legible
    fecha_legible = time.strftime("%d/%m/%Y", tiempo_local)
    
    return fecha_legible

def restablecer_variables(juego):
    juego["puntuacion"] = 0
    juego["vidas"] = CANTIDAD_VIDAS
    juego["acertados_seguidos"] = 1

def reproducir_sonido(sonido):
    sonido.play()

def controlar_comodin_bomba(bomba_sound, lista_preguntas, desaparecer_btn, juego, bomba_explotada):

    bomba_explotada = True 
    bomba_sound.play()
    respuesta = lista_preguntas[0]["correcta"]
    print(respuesta)

    botones_borrar = []

    for i in range(4):
        if not(i == int(respuesta)-1):
            boton = i
            botones_borrar.append(boton)
                
    botones_borrar.remove(random.choice(botones_borrar))

    for i in range(len(botones_borrar)):
                    

        if botones_borrar[i] == 0:
            desaparecer_btn["btn_respuesta1"] = True
        elif botones_borrar[i] == 1:
            desaparecer_btn["btn_respuesta2"] = True
        elif botones_borrar[i] == 2:
            desaparecer_btn["btn_respuesta3"] = True
        elif botones_borrar[i] == 3:
            desaparecer_btn["btn_respuesta4"] = True

    juego["bomba"] -= 1
    return bomba_explotada

def mostrar_texto_en_contenedor(contenedor: pygame.Surface, texto: str, fuente: pygame.font.Font = FUENTE_20):
    # Dividir el texto en palabras
    palabras = texto.split()
    lineas = []
    linea_actual = []
    ancho_contenedor = contenedor.get_width() - 80
        
    # Crear líneas que se ajusten al ancho
    for palabra in palabras:
        linea_prueba = ' '.join(linea_actual + [palabra])
        ancho_texto = fuente.size(linea_prueba)[0]

        if ancho_texto <= ancho_contenedor:
            linea_actual.append(palabra)
        else:
            lineas.append(' '.join(linea_actual))
            linea_actual = [palabra]
        
    if linea_actual:
        lineas.append(' '.join(linea_actual))
        
    # Calcular altura total del texto
    altura_linea = fuente.get_height()
    altura_total = len(lineas) * altura_linea
    
    # Posición inicial Y centrada
    y_inicial = (contenedor.get_height() - altura_total) // 2
    
    # Renderizar cada línea centrada
    for i in range(len(lineas)):
        superficie_texto = fuente.render(lineas[i], True, COLOR_AZUL)
        x_centrado = (contenedor.get_width() - superficie_texto.get_width()) // 2
        y_pos = y_inicial + (i * altura_linea)
        contenedor.blit(superficie_texto, (x_centrado, y_pos))
