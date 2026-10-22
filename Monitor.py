import time
import psutil

class MonitorRed:

    def __init__(self, umbral_kb, intervalo, alarma_obj):
        self.umbral = umbral_kb
        self.intervalo = intervalo
        self.alarma = alarma_obj
        self.ejecutando = False
        self.notificado = False

    def iniciar(self):
        self.ejecutando = True
        print("Monitoreando red...")
        while self.ejecutando:
            bytes_inicio = psutil.net_io_counters().bytes_recv
            time.sleep(self.intervalo)
            bytes_fin = psutil.net_io_counters().bytes_recv
            velocidad_kb = (bytes_fin - bytes_inicio) / 1024 / self.intervalo

            if velocidad_kb < self.umbral and not self.notificado:
                self.alarma.sonar()
                self.notificado = True
                
            elif velocidad_kb >= self.umbral:
                self.notificado = False