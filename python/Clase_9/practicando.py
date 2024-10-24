from pathlib import Path
import json

# Obtener la ruta del archivo Python actual y su directorio padre
ruta_actual = Path(__file__).parent

# Definir la ruta del archivo JSON utilizando el directorio actual
ruta_archivo = ruta_actual / "practica.json"



# Abrir el archivo en modo "w" (escritura) y asegurarse de que el archivo se crea si no existe
with ruta_archivo.open("w") as archivo:
    # Inicializar el archivo JSON con un contenido vacío o un objeto predeterminado
    json.dump({}, archivo)  # Por ejemplo, guardando un diccionario vacío

print(f"Archivo JSON creado en: {ruta_archivo.resolve()}")

