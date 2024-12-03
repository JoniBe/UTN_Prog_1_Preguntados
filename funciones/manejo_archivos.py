import os
import json
from modelos.pregunta import Pregunta
from modelos.respuesta import Respuesta
from modelos.puntaje import Puntaje
from constantes import PREGUNTAS_CSV_PATH, RANKING_JSON_PATH

def leer_csv_preguntas() -> list[Pregunta]:
    lista_preguntas = []
    
    if os.path.exists(PREGUNTAS_CSV_PATH):
        with open(PREGUNTAS_CSV_PATH,"r") as archivo:
            for linea in archivo:
                linea_aux = linea.replace("\n","")
                lista_valores = linea_aux.split(",")
                pregunta = lista_valores[0]
                lista_respuestas = []
                for respuesta in lista_valores[1:5]:
                    lista_respuestas.append(Respuesta(respuesta))
                respuesta_correcta = lista_valores[5]
                porcentaje_de_aciertos = lista_valores[6]
                cantidad_de_fallos = lista_valores[7]
                cantidad_de_aciertos = lista_valores[8]
                cantidad_de_veces_preguntada = lista_valores[9]
                nueva_pregunta = Pregunta(pregunta, lista_respuestas, respuesta_correcta, porcentaje_de_aciertos, cantidad_de_fallos, cantidad_de_aciertos, cantidad_de_veces_preguntada)
                lista_preguntas.append(nueva_pregunta)
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
    

def crear_dato_csv(diccionario:dict, separador:str) -> str:
    lista_valores = list(diccionario.values())
    for i in range(len(lista_valores)):
        lista_valores[i] = str(lista_valores[i])
    linea = separador.join(lista_valores)
    return linea

def guardar_csv(nombre_archivo:str, lista:list) -> bool:
    if type(lista) == list and len(lista) > 0:
        with open(nombre_archivo,"w") as archivo:
            for i in range(len(lista)):
                linea = crear_dato_csv(lista[i],",")
                if i != len(lista) -1:
                    archivo.write(linea + "\n")
                else:
                    archivo.write(linea)
        retorno = True
    else:
        retorno = False

    return retorno

def crear_pregunta_en_csv(pregunta: Pregunta, separador: str) -> str:
    linea = ""
    linea += pregunta.pregunta + separador
    for respuesta in pregunta.respuestas:
        linea += respuesta.respuesta + separador
    linea += str(pregunta.respuesta_correcta) + separador
    linea += str(pregunta.porcentaje_de_aciertos) + separador
    linea += str(pregunta.cantidad_de_fallos) + separador
    linea += str(pregunta.cantidad_de_aciertos) + separador
    linea += str(pregunta.cantidad_de_veces_preguntada)
    return linea

def actualizar_csv_de_preguntas(listado_preguntas: list[Pregunta]):
    if len(listado_preguntas) > 0:
        with open(PREGUNTAS_CSV_PATH, "w") as archivo:
            for i in range(len(listado_preguntas)):
                pregunta = listado_preguntas[i]
                linea = crear_pregunta_en_csv(pregunta, ",")
                if i != len(listado_preguntas) - 1:
                    archivo.write(linea + "\n")
                else:
                    archivo.write(linea)
        return True
    else:
        return False