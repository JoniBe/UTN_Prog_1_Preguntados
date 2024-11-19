

def leer_csv(archivo:str):

    lista = []

    with open(archivo) as file:

        for line in file.readlines():
            pregunta = line.split(",")
            diccionario = {"pregunta": pregunta[0].replace("Â",""), "respuesta_1" : pregunta[1], "respuesta_2" : pregunta[2], "respuesta_3" : pregunta[3], "respuesta_4" : pregunta[4].replace("\n", "")}
            lista.append(diccionario)
    return lista