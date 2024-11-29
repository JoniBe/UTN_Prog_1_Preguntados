import pygame
from modelos.ventana import Ventana
from modelos.menu_principal import MenuPrincipal
from Constantes import VENTANA_MENU_PRINCIPAL, VENTANA_SALIR, VENTANA_JUGAR, VENTANA_FIN_PARTIDA, FPS, CANTIDAD_VIDAS
from funciones.componentes import crear_lista_botones
from fin_de_partida import terminar_juego
from modelos.partida import Partida

pygame.mixer.init()
pygame.mixer.music.load("assets/cancion_juego.mp3")

ventana = Ventana().renderizar()

lista_botones = crear_lista_botones(ventana)

menu_principal = MenuPrincipal(lista_botones)

reloj = pygame.time.Clock()

corriendo = True

ventana_actual = VENTANA_MENU_PRINCIPAL

datos_juego = {
    "puntuacion": 0,
    "vidas": CANTIDAD_VIDAS,
    "usuario": "",
    "acertados_seguidos": 1,
    "tiempo": 60
}

partida = Partida(ventana)

while corriendo:
    cola_eventos = pygame.event.get()

    if ventana_actual == VENTANA_MENU_PRINCIPAL:
        ventana_actual = menu_principal.ejecutar(ventana, cola_eventos)
    elif ventana_actual == VENTANA_JUGAR:
        ventana_actual = partida.jugar(cola_eventos)
    elif ventana_actual == VENTANA_FIN_PARTIDA:
        ventana_actual = partida.terminar(cola_eventos)
    elif ventana_actual == VENTANA_SALIR:
        corriendo = False

    pygame.display.flip()
    
    reloj.tick(FPS)

# Finalizar el juego
pygame.quit()