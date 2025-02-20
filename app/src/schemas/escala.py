import enum

class Escala(str, enum.Enum):
    mucho = "mucho"
    moderado = "moderado"
    poco = "poco"
    nada = "nada"