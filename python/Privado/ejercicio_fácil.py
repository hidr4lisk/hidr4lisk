
# Ejercicio Fácil
# Descripción: Crea un programa que reciba una cadena de caracteres (string) y muestre la cantidad de caracteres que tiene.
# Luego, pide al usuario que ingrese dos palabras y muéstralas concatenadas.

# Instrucciones:
# 1. Pide al usuario que ingrese una cadena de texto y cuenta cuántos caracteres tiene.
# 2. Pide al usuario que ingrese dos palabras.
# 3. Muestra las dos palabras concatenadas.

cadena = input("Ingrese una cadena de texto: ")
print(f"La cadena tiene {len(cadena)} caracteres.")
palabra1 = input("Ingrese la primera palabra: ")
palabra2 = input("Ingrese la segunda palabra: ")
print(f"Las palabras concatenadas son: {palabra1 + palabra2}")
