from modelos.juego import Juego

juego = Juego()
juego.ejecutar()

# ventana = Ventana().renderizar()

# menu_principal = MenuPrincipal(ventana)

# reloj = pygame.time.Clock()

# corriendo = True

# ventana_actual = VENTANA_MENU_PRINCIPAL

# partida = Partida(ventana)

# while corriendo:
#     cola_eventos = pygame.event.get()

#     if ventana_actual == VENTANA_MENU_PRINCIPAL:
#         ventana_actual = menu_principal.ejecutar(cola_eventos, ventana_actual)
#     elif ventana_actual == VENTANA_JUGAR:
#         ventana_actual = partida.jugar(cola_eventos, ventana_actual)
#     elif ventana_actual == VENTANA_FIN_PARTIDA:
#         ventana_actual = partida.terminar(cola_eventos, ventana_actual)
#     elif ventana_actual == VENTANA_SALIR:
#         corriendo = False

#     pygame.display.flip()
    
#     reloj.tick(FPS)

# # Finalizar el juego
# pygame.quit()