from pathlib import Path

BASE_DIR = Path(__file__).parent #Parent va al directorio PADRE del archivo, o sea donde este

archivo = open(BASE_DIR / "7_escritura.txt", "w", encoding="UTF-8")
archivo.write("Este es un ejemplo de escritura Python.\n")
archivo.write("Esta es la segunda línea del archivo.\n")

otras_lineas = ["Esta es la tercera línea.\n", "Y esta es la cuarta línea.\n"]
for linea in otras_lineas:
    archivo.write(linea)
# archivo.writelines(otras_lineas)   # es lo mismo que hacer lo de arriba (for)

archivo.close()

