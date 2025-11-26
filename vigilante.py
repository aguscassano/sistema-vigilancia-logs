import time
import os
from datetime import datetime

ARCHIVO_LOG = os.path.join(os.getcwd(), "registro.log")

print(f"--- Iniciando servicio de vigilancia ---")
print(f"Escribiendo logs en: {ARCHIVO_LOG}")
print("Presiones Ctrl+C para detenerlo manualmente.")

while True:
	ahora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	mensaje = f"[ESTADO] El servidor sigue vivo a las: {ahora}\n"

	try:
		with open(ARCHIVO_LOG, "a") as f:
			f.write(mensaje)
	except Exception as e:
		print(f"Error escribiendo log: {e}")

	time.sleep(5)
