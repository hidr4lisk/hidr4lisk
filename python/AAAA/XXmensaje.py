import random
import os
import re

def desplazar_caracteres(texto, x):
    texto_desplazado = ""
    for caracter in texto:
        if caracter.isalpha():
            base = ord('A') if caracter.isupper() else ord('a')
            nuevo_caracter = chr((ord(caracter) - base + x) % 26 + base)
            texto_desplazado += nuevo_caracter
        else:
            texto_desplazado += caracter
    return texto_desplazado

def desplazar_caracteres_inverso(texto, x):
    texto_desplazado = ""
    for caracter in texto:
        if caracter.isalpha():
            base = ord('A') if caracter.isupper() else ord('a')
            nuevo_caracter = chr((ord(caracter) - base - x) % 26 + base)
            texto_desplazado += nuevo_caracter
        else:
            texto_desplazado += caracter
    return texto_desplazado

def leer_archivo(ruta_archivo):
    with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
        return archivo.read()

def guardar_archivo(ruta_archivo, texto):
    with open(ruta_archivo, 'w', encoding='utf-8') as archivo:
        archivo.write(texto)

# Programa principal
def main():
    while True:
        # Preguntamos al usuario si quiere cifrar o descifrar
        eleccion = input("Cifrar o Desifrar. 1 o 2: ").strip()
        
        if eleccion == "1":
            # Cifrado
            ruta_directorio = os.path.dirname(os.path.abspath(__file__))
            ruta_archivo = os.path.join(ruta_directorio, "a.txt")
            x = random.randint(1, 10)
            
            texto = leer_archivo(ruta_archivo)
            texto_desplazado = desplazar_caracteres(texto, x)
            
            nombre_archivo_salida = f"Readm3 ({x}).txt"
            ruta_salida = os.path.join(ruta_directorio, nombre_archivo_salida)
            guardar_archivo(ruta_salida, texto_desplazado)
            
            break  # Finalizamos tras cifrar
            
        elif eleccion == "2":
            # Descifrado
            ruta_directorio = os.path.dirname(os.path.abspath(__file__))
            patron_archivo = re.compile(r"Readm3 \((\d+)\)\.txt")
            
            archivo_desplazado = None
            for archivo in os.listdir(ruta_directorio):
                coincidencia = patron_archivo.match(archivo)
                if coincidencia:
                    archivo_desplazado = archivo
                    x = int(coincidencia.group(1))
                    break
            
            if archivo_desplazado:
                ruta_archivo = os.path.join(ruta_directorio, archivo_desplazado)
                texto = leer_archivo(ruta_archivo)
                texto_desplazado_inverso = desplazar_caracteres_inverso(texto, x)
                
                ruta_salida = os.path.join(ruta_directorio, "b.txt")
                guardar_archivo(ruta_salida, texto_desplazado_inverso)
            
            break  # Finalizamos tras descifrar
            
        else:
            continue  # Si la opción no es válida, vuelve a preguntar

# Ejecutamos el programa
main()