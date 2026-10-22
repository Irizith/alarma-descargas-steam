import winsound

class alarma:
    def __init__(self, Frecuencia, Duracion):
        self.frecuencia = Frecuencia
        self.duracion = Duracion
        self.ejecutando = False
    
    def sonar(self):
        self.ejecutando = True
        print(
            f"Alarma iniciando con Frecuencia de {self.frecuencia} Hz a {self.duracion} Ms"
            )
        for _ in range(1):
            winsound.Beep(self.frecuencia, self.duracion)

