from modelos.pregunta import Pregunta
from Constantes import PREGUNTAS_CSV_PATH
import os

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