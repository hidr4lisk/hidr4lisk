#Escribir un programa que pida al usuario dos números y muestre por pantalla su división. 
#Si el divisor es cero el programa debe mostrar un error.
numeros = []
for i in range(2):
    while True:
        try:
            if i == 0:
                numero = int(input("Ingrese el primer número: "))
            else:
                numero = int(input("Ingrese el segundo número: "))
            numeros.append(numero)  # Agregar el número válido a la lista
            break  # Salir del bucle si es válido
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero.")

# Verificar si el segundo número es cero
if numeros[1] == 0:
    print("No se puede dividir por 0.")
else:
    resultado = numeros[0] / numeros[1]
    print(f"La división entre esos números es: {resultado}")
