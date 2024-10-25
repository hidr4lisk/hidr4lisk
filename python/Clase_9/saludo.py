"""
Crear tres funciones: -
a) Una que imprima "¡Bienvenido!"
b) Otra que imprima "¡Adiós!".
c) Una tercera función llame a las dos funciones anteriores.
Debes invocar (o llamar) solamente a la tercera función para que se ejecuten las dos primeras.
"""

def saludo():
    print("¡Bienvenido!")

def despedida():
    print("¡Adiós!")

def elegi(eleccion):
    if eleccion == 1:
        saludo()
    else:
        despedida()

while True:
    elijamos = int(input("Ingrese una opcion\n1. para Saludar.\n2. para Despedirte.\nElija: "))
    if elijamos == 1:
        saludo()
        break
    elif elijamos == 2:
        despedida()
        break
    else: 
        continue