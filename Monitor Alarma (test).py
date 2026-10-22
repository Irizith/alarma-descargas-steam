import time
import psutil
import winsound

# --- PARÁMETROS DE CONFIGURACIÓN ---
UMBRAL_KB = 1000.0               # Velocidad mínima (KB/s). si cae de esto, cuenta como "baja"
SEGUNDOS_INTERVALO = 3          # Tiempo de espera entre cada medición
CONFIRMACIONES_REQUERIDAS = 4   # Cuántas mediciones bajas seguidas se necesitan para activar la alarma

print("=== MONITOR DESCARGA DE STEAM ===")
print(f"Monitoreando red... Alarma cuando la velocidad caiga de {UMBRAL_KB} KB/s.")
print("Presiona Ctrl + C para detener el programa manualmente.\n")

lecturas_bajas = 0

while True:
    # 1. Medimos el tráfico de red en el intervalo
    bytes_inicio = psutil.net_io_counters().bytes_recv
    time.sleep(SEGUNDOS_INTERVALO)
    bytes_fin = psutil.net_io_counters().bytes_recv

    # 2. Calculamos la velocida promedio en KB/s
    velocidad_kb = ((bytes_fin - bytes_inicio) / SEGUNDOS_INTERVALO) / 1024

    # 3. Comprobamos la velocidad
    if velocidad_kb < UMBRAL_KB:
        lecturas_bajas += 1
    else:
        lecturas_bajas = 0 # Si la velocidad sube de nuevo. reseteamos el contador

        print(f"Velocidad: {velocidad_kb: .2f} KB/s | Contador de alerta: {lecturas_bajas}/{CONFIRMACIONES_REQUERIDAS}")

    # 4. Si se cumple el límite de confirmaciones, dispara alarma
    if lecturas_bajas >= CONFIRMACIONES_REQUERIDAS:
        print("\n¡DESCARGA FINALIZADA! 🎮🔔")

        # Secuencia de 5 pitidos rápidos
        for _ in range(5):
            winsound.Beep(1000, 300)
            time.sleep(0.1)

        break
        