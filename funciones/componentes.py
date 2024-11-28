import pygame
from modelos.boton import Boton
from modelos.coordenada import Coordenada
from modelos.menu_principal import MenuPrincipal

# Botones
def crear_lista_botones(ventana: pygame.Surface) -> list[Boton]:
    lista_botones = []

    mitad_width_ventana = ventana.get_width() // 2

    lista_botones.append(Boton('Jugar', Coordenada(mitad_width_ventana, 100)))
    lista_botones.append(Boton('Configuracion', Coordenada(mitad_width_ventana, 200)))
    lista_botones.append(Boton('Salir', Coordenada(mitad_width_ventana, 300)))

    return lista_botones