import random
import pygame

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



def mostrar_texto(surface, text, pos, font, color=pygame.Color('black')):
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, False, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.

