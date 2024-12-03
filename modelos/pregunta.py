from modelos.respuesta import Respuesta

# Pregunta
class Pregunta:
    def __init__(self, pregunta: str, respuestas: list[Respuesta], respuesta_correcta: int, porcentaje_de_aciertos: int, cantidad_de_fallos: int, cantidad_de_aciertos: int, cantidad_de_veces_preguntada: int):
        self.pregunta = pregunta
        self.respuestas = respuestas
        self.respuesta_correcta = int(respuesta_correcta)
        self.porcentaje_de_aciertos = float(porcentaje_de_aciertos)
        self.cantidad_de_fallos = int(cantidad_de_fallos)
        self.cantidad_de_aciertos = int(cantidad_de_aciertos)
        self.cantidad_de_veces_preguntada = int(cantidad_de_veces_preguntada)

    def validar_respuesta(self, respuesta: str) -> bool:
        respuesta_correcta_texto = self.respuestas[self.respuesta_correcta - 1].respuesta
        return respuesta.upper() == respuesta_correcta_texto.upper()
    
    def recalcular_contadores(self, es_acierto: bool):
        self.cantidad_de_veces_preguntada += 1
        if es_acierto:
            self.cantidad_de_aciertos += 1
        else:
            self.cantidad_de_fallos += 1
        self.porcentaje_de_aciertos = (self.cantidad_de_aciertos / self.cantidad_de_veces_preguntada) * 100
