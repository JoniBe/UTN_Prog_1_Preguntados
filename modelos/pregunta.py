from modelos.respuesta import Respuesta

# Pregunta
class Pregunta:
    def __init__(self, pregunta: str, respuestas: list[Respuesta], respuesta_correcta: int):
        self.pregunta = pregunta
        self.respuestas = respuestas
        self.respuesta_correcta = int(respuesta_correcta)

    def validar_respuesta(self, respuesta: str) -> bool:
        respuesta_correcta_texto = self.respuestas[self.respuesta_correcta - 1].respuesta
        return respuesta.upper() == respuesta_correcta_texto.upper()
