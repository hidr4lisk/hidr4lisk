#Actividad 1 - Hay tabla
#Escribe un programa que tome un número entero positivo ingresado por el usuario y muestre la tabla de multiplicar de ese número. Repite la solicitud al usuario de ingresar un nuevo número hasta que ingrese un cero.


while True:
    num = int(input("Ingrese un número para conocer su Tabla:  "))
    if num == 0:
        break
    for i in range(10):
        multi = num * (i +1)
        print(f"{num} * {i+1} = {multi}")

