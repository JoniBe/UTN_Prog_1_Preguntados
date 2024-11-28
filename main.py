import pygame
from modelos.ventana import Ventana
from modelos.menu_principal import MenuPrincipal
from modelos.boton import Boton
from constantes import VENTANA_MENU_PRINCIPAL, VENTANA_SALIR, FPS
from funciones.componentes import crear_lista_botones

ventana_actual = VENTANA_MENU_PRINCIPAL

corriendo = True

ventana = Ventana().renderizar()

lista_botones = crear_lista_botones(ventana)

menu_principal = MenuPrincipal(lista_botones)

reloj = pygame.time.Clock()

while corriendo:
    reloj.tick(FPS)

    cola_eventos = pygame.event.get()

    if ventana_actual == VENTANA_MENU_PRINCIPAL:
        ventana_actual = menu_principal.ejecutar(ventana, cola_eventos)
    elif ventana_actual == VENTANA_SALIR:
        corriendo = False

    pygame.display.flip()

# Finalizar el juego
pygame.quit()