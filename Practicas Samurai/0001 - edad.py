#Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.
edad = -1
while True:
    try:
        edad = int(input("Ingrese su edad: "))
        if edad > 0:
            break
        else:
            print("Por favor, ingrese un número entero mayor a 0.")
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número entero.")


if edad >= 18:
    print("Es mayor de Edad")
else:
    print("Es menor de Edad")