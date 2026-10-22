from Alarma import alarma
from Monitor import MonitorRed

mi_alarma = alarma(Frecuencia=1000, Duracion=300)
mi_monitor = MonitorRed(umbral_kb=500, intervalo=1, alarma_obj=mi_alarma)

print("Presiona Ctrl + C para detener el programa manualmente.\n")

try:
    mi_monitor.iniciar()
except KeyboardInterrupt:
    print("\nMonitoreo detenido por el usuario. 👋")   
