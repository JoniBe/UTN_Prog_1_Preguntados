import pygame
from Constantes import VENTANA_MEDIDA, BACKGROUND_MENU_PRINCIPAL

# Ventana
class Ventana:
    def __init__(self):
        self.caption = 'PREGUNTADOS'
        self.medida = VENTANA_MEDIDA
        self.background_menu_principal = pygame.transform.scale(BACKGROUND_MENU_PRINCIPAL, VENTANA_MEDIDA)

    def renderizar(self) -> pygame.Surface:
        pygame.display.set_caption(self.caption)
        ventana = pygame.display.set_mode(self.medida)
        background = pygame.transform.scale(self.background_menu_principal, self.medida)
        ventana.blit(background, (0, 0))

        return ventana
