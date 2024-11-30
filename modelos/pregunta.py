# Pregunta
class Pregunta:
    def __init__(self, pregunta: str, opciones: list[str], respuesta_correcta: int):
        self.pregunta = pregunta
        self.opciones = opciones
        self.respuesta_correcta = int(respuesta_correcta)

    def validar_respuesta(self, respuesta: int) -> bool:
        return respuesta == self.respuesta_correcta