#Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.

numero = -1
while True:
    try:
        numero = int(input('Ingrese un numeró: '))
        break
    except ValueError:
        print("Error, ingreso no válido.")

paridad = numero % 2
if paridad != 0:
    print("No es par")
else:
    print("es par")