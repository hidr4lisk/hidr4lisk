#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.

# Pedir al usuario un número entero positivo
while True:
    try:
        numero = int(input("Ingrese un número entero positivo: "))
        if numero > 0:
            break
    except ValueError:
        print("Por favor, ingrese un número válido.")
# Generar la cuenta atrás y almacenarla en una lista
lista = [i for i in range(numero, -1, -1)]
# Mostrar la lista separada por comas
print(", ".join(map(str, lista)))

