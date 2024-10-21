"""
Escribir una funcion que reciba una cantidad de interacciones de una tirada de 2 dados a realizar y devuelva la cantidad de veces que se observa cada valor de la suma de los 2 dados. 

Determinar que el dado se tira un minimo de 3 veces.

Nota: utilizar el modulo random para obtener tiradas alteatorias.
import random

#simular una tirada de un dado de 6 caras 
tirada_dado = random.randint(1,6)
print(tirada_dados)
"""
import random

def dados(tiros):
    suma = []
    for i in range(tiros):
        dado1 = random.randint(1, 6)
        dado2 = random.randint(1, 6)
        suma.append(dado1 + dado2)
    return suma

while True:
    try:
        arrojar_dados = int(input("Ingrese la cantidad de intentos (deben ser mínimo 3): "))
        if arrojar_dados < 3:
            print("Por favor, ingrese un número mayor o igual a 3.")
        else:
            break  # Salimos del bucle si la entrada es válida
    except ValueError:
        print("Entrada no válida. Debe ingresar un número entero.")

# Realizamos las tiradas de dados
tiradas = dados(arrojar_dados)
resultados = {i: 0 for i in range(2, 13)} #para armar el diccionario con las posibilidades
for valor in tiradas:
    resultados[valor] += 1
print(f"Tiradas: {tiradas}")
print("Cantidad de veces que se observó cada suma:")
for valor, cantidad in resultados.items():
    print(f"Suma {valor}: {cantidad} veces")