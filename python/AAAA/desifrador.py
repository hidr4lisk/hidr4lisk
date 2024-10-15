import os
import re

def desplazar_caracteres_inverso(texto, x):
    texto_desplazado = ""
    
    for caracter in texto:
        if caracter.isalpha():  # Solo desplazamos letras
            # Verificamos si es mayúscula o minúscula
            base = ord('A') if caracter.isupper() else ord('a')
            # Calculamos el nuevo carácter desplazado inversamente dentro del rango alfabético
            nuevo_caracter = chr((ord(caracter) - base - x) % 26 + base)
            texto_desplazado += nuevo_caracter
        else:
            # Si no es letra, no lo desplazamos
            texto_desplazado += caracter
    
    return texto_desplazado

# Leemos el archivo de texto
def leer_archivo(ruta_archivo):
    with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
        return archivo.read()

# Guardamos el texto desplazado en un nuevo archivo
def guardar_archivo(ruta_archivo, texto):
    with open(ruta_archivo, 'w', encoding='utf-8') as archivo:
        archivo.write(texto)

# Programa principal

# Obtenemos la ruta absoluta del directorio donde está el archivo .py
ruta_directorio = os.path.dirname(os.path.abspath(__file__))

# Buscamos archivos "Readm3 (X).txt"
patron_archivo = re.compile(r"Readm3 \((\d+)\)\.txt")

# Encontramos el archivo que coincide con el patrón
archivo_desplazado = None
for archivo in os.listdir(ruta_directorio):
    coincidencia = patron_archivo.match(archivo)
    if coincidencia:
        archivo_desplazado = archivo
        x = int(coincidencia.group(1))  # Extraemos el valor de X del nombre del archivo
        break

if archivo_desplazado:
    print(f"Archivo encontrado: {archivo_desplazado} con desplazamiento {x}.")

    # Leemos el archivo "Readm3 (X).txt"
    ruta_archivo = os.path.join(ruta_directorio, archivo_desplazado)
    texto = leer_archivo(ruta_archivo)

    # Desplazamos el texto inversamente
    texto_desplazado_inverso = desplazar_caracteres_inverso(texto, x)

    # Guardamos el texto desplazado en un nuevo archivo con el nombre "Restaurado.txt"
    ruta_salida = os.path.join(ruta_directorio, "Restaurado.txt")
    guardar_archivo(ruta_salida, texto_desplazado_inverso)

    print(f"El texto ha sido restaurado y guardado en {ruta_salida}.")
else:
    print("No se encontró un archivo 'Readm3 (X).txt' en la carpeta.")
