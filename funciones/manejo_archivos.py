import modelos as modelos
import constantes
import os

def leer_csv_preguntas() -> list[modelos.Pregunta]:
    lista_preguntas = []
    
    if os.path.exists(constantes.PREGUNTAS_CSV_PATH):
        # Falsa lectura -> Para evitar recorrer en el for de abajo, la cabecera
        archivo.readline()

        with open(constantes.PREGUNTAS_CSV_PATH,"r") as archivo:
            for linea in archivo:
                linea_aux = linea.replace("\n","")
                lista_valores = linea_aux.split(",")
                mi_pregunta = modelos.Pregunta(lista_valores[0],lista_valores[1:5],lista_valores[5])
                lista_preguntas.append(mi_pregunta)
    else:
        return False
    
    return lista_preguntas