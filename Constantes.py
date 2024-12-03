import pygame

pygame.init()

# CONFIGURACIONES
FPS = 60
VENTANA_WIDTH = 800
VENTANA_HEIGHT = 800
VENTANA_MEDIDA = (VENTANA_WIDTH, VENTANA_HEIGHT)
VENTANA_CENTRO_WIDTH = VENTANA_WIDTH // 2
VENTANA_CENTRO_HEIGHT = VENTANA_HEIGHT // 2

# JUEGO
TIEMPO_INICIAL = 60
CANTIDAD_VIDAS = 3
PUNTUACION_ACIERTO = 100
PUNTUACION_ERROR = 50
MAX_ACIERTOS_SEGUIDOS = 3
VIDA_EXTRA_POR_ACIERTOS_SEGUIDOS = 1
TIEMPO_EXTRA_POR_ACIERTOS_SEGUIDOS = 20
CANTIDAD_COMODIN_BOMBA = 3
CANTIDAD_COMODIN_X2 = 3
CANTIDAD_COMODIN_PASAR = 3
CANTIDAD_COMODIN_DOBLE_CHANCE = 3
COMODIN_TIPO_BOMBA = "BOMBA"
COMODIN_TIPO_X2 = "X2"
COMODIN_TIPO_PASAR = "PASAR"
COMODIN_TIPO_DOBLE_CHANCE = "DOBLE_CHANCE"

# VENTANAS
VENTANA_MENU_PRINCIPAL = 'MENU_PRINCIPAL'
VENTANA_JUGAR = 'JUGAR'
VENTANA_PARTIDA_FINALIZADA = 'PARTIDA_FINALIZADA'
VENTANA_RANKING = 'RANKING'
VENTANA_CONFIGURACION = 'CONFIGURACION'
VENTANA_SALIR = 'SALIR'

# COLORES
COLOR_BLANCO = (255,255,255)
COLOR_NEGRO = (0,0,0)
COLOR_VERDE = (0,255,0)
COLOR_ROJO = (255,0,0)
COLOR_AZUL = (0,0,255)
COLOR_VIOLETA = (134,23,219)

# MENU PRINCIPAL
MENU_PRINCIPAL_TITULO = "PREGUNTADOS"
MENU_PRINCIPAL_TITULO_COLOR = (64, 174, 120)
MENU_PRINCIPAL_TITULO_COLOR_SOMBRA = (45, 122, 84)

# RANKING
RANKING_TITULO = "RANKING - TOP 10"
RANKING_TITULO_COLOR = (255, 255, 255)
RANKING_TITULO_COLOR_SOMBRA = (0, 0, 0)

# CONFIGURACION
CONFIGURACION_TITULO = "CONFIGURACION"
CONFIGURACION_TITULO_COLOR = (255, 255, 255)
CONFIGURACION_TITULO_COLOR_SOMBRA = (0, 0, 0)

# BACKGROUNDS - PATHS
BACKGROUND_MENU_PRINCIPAL_PATH = "assets/background_menu_principal.jpg"
BACKGROUND_PARTIDA_PATH = "assets/background_partida.jpg"
BACKGROUND_PARTIDA_TERMINADA_PATH = "assets/background_partida_terminada.jpeg"
BACKGROUND_RANKING_PATH = "assets/background_ranking.jpg"
BACKGROUND_CONFIGURACION_PATH = "assets/background_configuracion.jpeg"

# BACKGROUNDS - RECURSOS
BACKGROUND_MENU_PRINCIPAL = pygame.image.load(BACKGROUND_MENU_PRINCIPAL_PATH)
BACKGROUND_PARTIDA = pygame.image.load(BACKGROUND_PARTIDA_PATH)
BACKGROUND_PARTIDA_TERMINADA = pygame.image.load(BACKGROUND_PARTIDA_TERMINADA_PATH)
BACKGROUND_RANKING = pygame.image.load(BACKGROUND_RANKING_PATH)
BACKGROUND_CONFIGURACION = pygame.image.load(BACKGROUND_CONFIGURACION_PATH)

# CONTENEDORES - PATHS
MENU_CONTENEDOR_PATH = "assets/menu_contenedor.png"
CONTENEDOR_PREGUNTA_PATH = "assets/contenedor_pregunta.png"
CONTENEDOR_TIEMPO_PATH = "assets/contenedor_redondo_gris.png"
CONTENEDOR_VIDAS_PATH = "assets/contenedor_gris.png"
CONTENEDOR_PUNTUACION_PATH = "assets/contenedor_gris.png"
RANKING_CONTENEDOR_PATH = "assets/ranking_contenedor.png"
CONTENEDOR_COMODIN_PATH = "assets/contenedor_comodin.png"

# CONTENEDORES - RECURSOS
MENU_CONTENEDOR = pygame.image.load(MENU_CONTENEDOR_PATH)
CONTENEDOR_PREGUNTA = pygame.image.load(CONTENEDOR_PREGUNTA_PATH)
CONTENEDOR_TIEMPO = pygame.image.load(CONTENEDOR_TIEMPO_PATH)
CONTENEDOR_VIDAS = pygame.image.load(CONTENEDOR_VIDAS_PATH)
CONTENEDOR_PUNTUACION = pygame.image.load(CONTENEDOR_PUNTUACION_PATH)
RANKING_CONTENEDOR = pygame.image.load(RANKING_CONTENEDOR_PATH)
CONTENEDOR_COMODIN = pygame.image.load(CONTENEDOR_COMODIN_PATH)

# BOTONES - PATHS
CONTENEDOR_BOTON_VOLUMEN_PATH = "assets/contenedor_boton_volumen.png"
BOTON_VERDE_PATH = "assets/boton_verde.png"
BOTON_AZUL_PATH = "assets/boton_azul.png"
BOTON_VOLUMEN_MAS_PATH = "assets/volumen_mas.png"
BOTON_VOLUMEN_MENOS_PATH = "assets/volumen_menos.png"
BOTON_VOLUMEN_MUTEAR_PATH = "assets/volumen_mutear.png"
BOTON_VOLUMEN_DESMUTEAR_PATH = "assets/volumen_desmutear.png"

# BOTONES - RECURSOS
CONTENEDOR_BOTON_VOLUMEN = pygame.image.load(CONTENEDOR_BOTON_VOLUMEN_PATH)
BOTON_VERDE = pygame.image.load(BOTON_VERDE_PATH)
BOTON_AZUL = pygame.image.load(BOTON_AZUL_PATH)
BOTON_VOLUMEN_MAS = pygame.image.load(BOTON_VOLUMEN_MAS_PATH)
BOTON_VOLUMEN_MENOS = pygame.image.load(BOTON_VOLUMEN_MENOS_PATH)
BOTON_VOLUMEN_MUTEAR = pygame.image.load(BOTON_VOLUMEN_MUTEAR_PATH)
BOTON_VOLUMEN_DESMUTEAR = pygame.image.load(BOTON_VOLUMEN_DESMUTEAR_PATH)

# BOTONES - CONFIGURACIONES
BOTON_ESCALADO_ALTO = 50
BOTON_ESCALADO_ANCHO = 250
BOTON_TIPO_MENU = "MENU"
BOTON_TIPO_RESPUESTA = "RESPUESTA"
BOTON_TIPO_VOLVER = "VOLVER"
BOTON_TIPO_VOLUMEN = "VOLUMEN"

# CAMPOS - PATHS
CAMPO_USUARIO_PATH = "assets/campo_usuario.png"

# CAMPOS - RECURSOS
CAMPO_USUARIO = pygame.image.load(CAMPO_USUARIO_PATH)

# SONIDOS - PATHS
MUSICA_JUEGO_PATH = "assets/cancion_juego.mp3"
SONIDO_ACIERTO_PATH = "assets/sonido_acierto.mp3"
SONIDO_ERROR_PATH = "assets/sonido_error.mp3"
SONIDO_EXPLOSION_PATH = "assets/explosion.mp3"
SONIDO_COMODIN_PATH = "assets/sonido_comodin.mp3"

# SONIDOS - RECURSOS
SONIDO_ACIERTO = pygame.mixer.Sound(SONIDO_ACIERTO_PATH)
SONIDO_ERROR = pygame.mixer.Sound(SONIDO_ERROR_PATH)
SONIDO_EXPLOSION = pygame.mixer.Sound(SONIDO_EXPLOSION_PATH)
SONIDO_COMODIN = pygame.mixer.Sound(SONIDO_COMODIN_PATH)

# FUENTES - PATHS
FUENTE_PATH = "assets/kenney_future.ttf"

# FUENTES - RECURSOS
FUENTE_16 = pygame.font.Font(FUENTE_PATH, 16)
FUENTE_20 = pygame.font.Font(FUENTE_PATH, 20)
FUENTE_30 = pygame.font.Font(FUENTE_PATH, 30)
FUENTE_40 = pygame.font.Font(FUENTE_PATH, 40)
FUENTE_50 = pygame.font.Font(FUENTE_PATH, 50)
FUENTE_60 = pygame.font.Font(FUENTE_PATH, 60)

# ARCHIVOS - PATHS
PREGUNTAS_CSV_PATH = "data/preguntas.csv"
RANKING_JSON_PATH = "data/puntos.json"

# COMODINES - PATHS
COMODIN_BOMBA_PATH = "assets/bomba.png"
COMODIN_PASAR_PATH = "assets/pasar.png"
COMODIN_X2_PATH = "assets/x2.png"
COMODIN_DOBLE_CHANCE_PATH = "assets/doble_chance.png"

# COMODINES - RECURSOS
COMODIN_BOMBA = pygame.image.load(COMODIN_BOMBA_PATH)
COMODIN_PASAR = pygame.image.load(COMODIN_PASAR_PATH)
COMODIN_X2 = pygame.image.load(COMODIN_X2_PATH)
COMODIN_DOBLE_CHANCE = pygame.image.load(COMODIN_DOBLE_CHANCE_PATH)
