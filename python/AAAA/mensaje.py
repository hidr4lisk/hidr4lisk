import random
import os
import re
import sys

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

# Función para obtener el directorio correcto en ejecución compilada
def obtener_directorio():
    if getattr(sys, 'frozen', False):
        # Si está congelado con PyInstaller
        return sys._MEIPASS
    else:
        # Si se está ejecutando como script
        return os.path.dirname(os.path.abspath(__file__))

def main():
    while True:
        eleccion = input("Cifrar o Desifrar. 1 o 2: ").strip()
        
        if eleccion == "1":
            print("Iniciando cifrado...")
            ruta_directorio = obtener_directorio()
            ruta_archivo = os.path.join(ruta_directorio, "a.txt")
            x = random.randint(1, 10)
            print(f"Desplazamiento elegido: {x}")
            
            try:
                texto = leer_archivo(ruta_archivo)
                print("Archivo leído correctamente.")
                texto_desplazado = desplazar_caracteres(texto, x)
                
                nombre_archivo_salida = f"Readm3 ({x}).txt"
                ruta_salida = os.path.join(os.path.dirname(os.path.abspath(__file__)), nombre_archivo_salida)
                guardar_archivo(ruta_salida, texto_desplazado)
                print(f"Texto cifrado guardado en: {ruta_salida}")
                break
                
            except FileNotFoundError:
                print(f"Error: El archivo '{ruta_archivo}' no fue encontrado.")
                break
            
        elif eleccion == "2":
            print("Iniciando descifrado...")
            ruta_directorio = obtener_directorio()
            patron_archivo = re.compile(r"Readm3 \((\d+)\)\.txt")
            
            archivo_desplazado = None
            x = None
            
            for archivo in os.listdir(os.path.dirname(os.path.abspath(__file__))):
                coincidencia = patron_archivo.match(archivo)
                if coincidencia:
                    archivo_desplazado = archivo
                    x = int(coincidencia.group(1))
                    print(f"Archivo encontrado para descifrar: {archivo_desplazado}")
                    break
            
            if archivo_desplazado and x is not None:
                ruta_archivo = os.path.join(os.path.dirname(os.path.abspath(__file__)), archivo_desplazado)
                texto = leer_archivo(ruta_archivo)
                texto_desplazado_inverso = desplazar_caracteres_inverso(texto, x)
                
                ruta_salida = os.path.join(os.path.dirname(os.path.abspath(__file__)), "b.txt")
                guardar_archivo(ruta_salida, texto_desplazado_inverso)
                print(f"Texto descifrado guardado en: {ruta_salida}")
            else:
                print("Error: No se encontró un archivo válido para descifrar.")
                
            break
        
        else:
            print("Opción no válida. Por favor, elige 1 o 2.")

if __name__ == "__main__":
    main()
