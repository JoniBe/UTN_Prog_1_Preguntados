import pygame
from Constantes import VENTANA_MEDIDA

# Ventana
class Ventana:
    def __init__(self):
        self.caption = 'PREGUNTADOS'

    def renderizar(self) -> pygame.Surface:
        pygame.display.set_caption(self.caption)
        ventana = pygame.display.set_mode(VENTANA_MEDIDA)

        return ventana
