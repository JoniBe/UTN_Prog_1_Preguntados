import pygame
from constantes import *
from modelos.boton import Boton
from modelos.coordenada import Coordenada

# Botones
def crear_lista_botones(ventana: pygame.Surface) -> list[Boton]:
    lista_botones = []

    mitad_width_ventana = ventana.get_width() // 2

    lista_botones.append(Boton('Jugar', Coordenada(mitad_width_ventana, 100)))
    lista_botones.append(Boton('Configuracion', Coordenada(mitad_width_ventana, 200)))
    lista_botones.append(Boton('Salir', Coordenada(mitad_width_ventana, 300)))

    return lista_botones

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