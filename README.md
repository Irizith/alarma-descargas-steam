Un `README.md` limpio y bien presentado le da a tu proyecto una apariencia 100% profesional en GitHub.

Copia y reemplaza el contenido de tu archivo **`README.md`** con la siguiente estructura:

```markdown
# 🔔 Monitor de Descargas de Red / Steam

Un script modular en Python diseñado para monitorear el ancho de banda entrante en tiempo real y emitir una alerta sonora si la velocidad cae por debajo de un umbral configurado. Ideal para avisar cuando una descarga en segundo plano finaliza o si la velocidad se interrumpe.

## 🚀 Características
- **Notificación de estado inteligente:** La alarma suena solo **una vez** al caer por debajo del umbral y se rearma automáticamente cuando la velocidad de descarga se recupera.
- **Arquitectura modular:** Separación de responsabilidades limpia entre lógica de monitoreo, sonido y ejecución.
- **Cierre suave:** Manejo elegante de interrupciones con `Ctrl + C` (`KeyboardInterrupt`) para salir de la aplicación sin arrojar trazas de error en la terminal.

## 🛠️ Requisitos
- Windows OS (requerido para la librería nativa `winsound`).
- Python 3.8 o superior.
- Librería `psutil`.

## 📦 Instalación

1. Clona el repositorio:
   ```bash
   git clone [https://github.com/Irizith/alarma-descargas-steam.git](https://github.com/Irizith/alarma-descargas-steam.git)
   cd alarma-descargas-steam

```

2. Instala la dependencia requerida:
```bash
pip install psutil

```



## 📄 Estructura del Proyecto

| Archivo | Descripción |
| --- | --- |
| **`alarma.py`** | Define la clase `alarma` que gestiona la emisión de sonido (`winsound.Beep`). |
| **`Monitor.py`** | Define la clase `MonitorRed`, la medición de red con `psutil` y la lógica de la bandera de estado. |
| **`MainMonitor.py`** | Punto de entrada principal que instancía los componentes y controla la ejecución. |

## 💻 Uso

Ejecuta el archivo principal desde tu terminal:

```bash
python MainMonitor.py

```

Para detener el monitoreo en cualquier momento, presiona `Ctrl + C` en la terminal.

```