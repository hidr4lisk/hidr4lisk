#Actividad 2 - x 3, x 5
#Escribe un programa que tome un número entero ingresado por el usuario y determine si es un número par, divisible por 3 y 5 al mismo tiempo, o ninguno de los anteriores.

numero = int(input("Ingrese un número: "))
if numero % 2 == 0 and numero % 3 == 0 and numero % 5 == 0:
    print("Cumple las condiciones, es divisible por 2, 3 y 5")
else:
    print("No cumple la condición")