import random
import os

def desplazar_caracteres(texto, x):
    texto_desplazado = ""
    
    for caracter in texto:
        if caracter.isalpha():  # Solo desplazamos letras
            # Verificamos si es mayúscula o minúscula
            base = ord('A') if caracter.isupper() else ord('a')
            # Calculamos el nuevo carácter desplazado dentro del rango alfabético
            nuevo_caracter = chr((ord(caracter) - base + x) % 26 + base)
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

# Creamos la ruta absoluta para "a.txt"
ruta_archivo = os.path.join(ruta_directorio, "a.txt")

# Generamos un número aleatorio entre 1 y 10 para X
x = random.randint(1, 10)
print(f"El número de desplazamientos aleatorio es: {x}")

# Leemos el archivo "a.txt"
texto = leer_archivo(ruta_archivo)

# Desplazamos el texto
texto_desplazado = desplazar_caracteres(texto, x)

# Guardamos el texto desplazado en un archivo con el nombre "Readm3 (X).txt" en el mismo directorio
nombre_archivo_salida = f"Readm3 ({x}).txt"
ruta_salida = os.path.join(ruta_directorio, nombre_archivo_salida)
guardar_archivo(ruta_salida, texto_desplazado)

print(f"El texto ha sido desplazado {x} posiciones y guardado en {ruta_salida}.")
