# 🎮 Monitor y Alarma de Descargas para Steam

Un script liviano en Python que monitorea el uso de red de la computadora en tiempo real y dispara una alerta sonora cuando detecta que una descarga de Steam ha finalizado.

## 🚀 Características
- **Monitoreo dinámico:** Mide el consumo de red global utilizando la librería `psutil`.
- **Prevención de falsos positivos:** Requiere múltiples lecturas consecutivas por debajo del umbral antes de activar la alarma.
- **Sin dependencias pesadas:** Utiliza el módulo nativo `winsound` de Windows para las alertas sonoras.

## 🛠️ Requisitos e Instalación
1. Tener instalado Python 3.x.
2. Instalar la librería requerida:
   ```bash
   pip install psutil

## 💻 Uso
1. Abre la consola en la carpeta del proyecto y ejecuta:
   ```bash
   python alarma.py