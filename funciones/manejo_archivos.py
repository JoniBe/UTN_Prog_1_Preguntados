import os
import json
from modelos.pregunta import Pregunta
from modelos.puntaje import Puntaje
from Constantes import PREGUNTAS_CSV_PATH, RANKING_JSON_PATH

def leer_csv_preguntas() -> list[Pregunta]:
    lista_preguntas = []
    
    if os.path.exists(PREGUNTAS_CSV_PATH):
        with open(PREGUNTAS_CSV_PATH,"r") as archivo:
            for linea in archivo:
                linea_aux = linea.replace("\n","")
                lista_valores = linea_aux.split(",")
                mi_pregunta = Pregunta(lista_valores[0], lista_valores[1:5],lista_valores[5])
                lista_preguntas.append(mi_pregunta)
    else:
        return False
    
    return lista_preguntas

def leer_json_ranking() -> list[Puntaje]:
    lista_ranking = []
    if os.path.exists(RANKING_JSON_PATH):
        with open(RANKING_JSON_PATH,"r") as archivo:
            listado = json.load(archivo)
            for puntaje in listado:
                puntaje_aux = Puntaje(puntaje["puntos"], puntaje["fecha"], puntaje["nombre"])
                lista_ranking.append(puntaje_aux)
        return lista_ranking
    else:
        return []