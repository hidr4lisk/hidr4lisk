#Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.
palabra = input("Ingrese la palabra que quiere repetir: ")
for i in range(10):
    print(f"{palabra} {i}")