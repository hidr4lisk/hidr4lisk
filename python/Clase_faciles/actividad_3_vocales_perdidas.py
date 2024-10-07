#Actividad 3 - ¿Vocales perdidas?
#Crea un programa que solicite al usuario ingresar una palabra. Luego, recorre la palabra y cuenta cuántas vocales contiene. Al final, si no se encontraron vocales, muestra un mensaje comunicando que la palabra ingresada solo contiene consonantes.
#Podemos utilizar el operador ‘in’ para corroborar si tiene vocales o no 

palabra = input("Ingrese una palabra: ")
vocales = ("a","e","i","o","u")
cantidad = 0
for letra in palabra.lower():
    if letra in vocales: cantidad += 1
if cantidad == 0: 
    print(f"No hay Vocales, solo consonantes en \"{palabra}\"")
else:
    print(f"Hay {cantidad} Vocales en \"{palabra}\"")
