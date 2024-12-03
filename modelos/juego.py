import pygame
from constantes import *
from modelos.ventana import Ventana
from modelos.partida import Partida
from modelos.partida_finalizada import PartidaFinalizada
from modelos.menu_principal import MenuPrincipal
from modelos.ranking import Ranking
from modelos.configuracion import Configuracion

# Juego
class Juego:
    def __init__(self):
        self.ventana_actual = VENTANA_MENU_PRINCIPAL
        self.ventana = Ventana().renderizar()
        self.menu_principal = MenuPrincipal(self.ventana)
        self.partida = Partida(self.ventana)
        self.partida_finalizada = PartidaFinalizada(self.ventana)
        self.ranking = Ranking(self.ventana)
        self.configuracion = Configuracion(self.ventana)
        self.reloj = pygame.time.Clock()
        self.corriendo = True

    def ejecutar_musica(self):
        pygame.mixer.init()
        pygame.mixer.music.load(MUSICA_JUEGO_PATH)
        pygame.mixer.music.play(-1)

    def ejecutar(self):
        self.ejecutar_musica()

        while self.corriendo:
            cola_eventos = pygame.event.get()

            if self.ventana_actual == VENTANA_MENU_PRINCIPAL:
                self.ventana_actual = self.menu_principal.ejecutar(cola_eventos, self.ventana_actual)
            elif self.ventana_actual == VENTANA_JUGAR:
                self.ventana_actual = self.partida.jugar(cola_eventos, self.ventana_actual)
            elif self.ventana_actual == VENTANA_PARTIDA_FINALIZADA:
                self.ventana_actual = self.partida_finalizada.mostrar(cola_eventos, self.ventana_actual, self.partida)
            elif self.ventana_actual == VENTANA_RANKING:
                self.ventana_actual = self.ranking.mostrar(cola_eventos, self.ventana_actual)
            elif self.ventana_actual == VENTANA_CONFIGURACION:
                self.ventana_actual = self.configuracion.mostrar(cola_eventos, self.ventana_actual)
            elif self.ventana_actual == VENTANA_SALIR:
                self.corriendo = False

            pygame.display.flip()

            self.reloj.tick(FPS)

        self.finalizar()
    
    def finalizar(self):
        pygame.quit()
