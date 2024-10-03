#Actividad 3 - ¡Positivo! ¿Par sí o par no?
#Crea un programa que solicite un número entero al usuario y determine si es un número negativo, positivo o igual a cero. En caso de ser positivo, verifica si es par o impar.

#primero pedimos el ingreso del número:
numero = int(input("Ingrese un número: "))

#ahora verificamos: resultado
if numero == 0:
    resultado = "Cero"
else:
    if numero < 0:
        resultado = "Negativo"
    else:
        if numero % 2 == 0:
            resultado = "Positivo y Par"
        else:
            resultado = "Positivo Impar"

print(resultado)