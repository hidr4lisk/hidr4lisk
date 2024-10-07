def ingresar():
    while True:
        entrada = input("Por favor, ingresa un número mayor que 1: ")
        if entrada.isdigit() and int(entrada) > 1:  # Verifica si la entrada es un número entero mayor a 1
            return int(entrada)
        else:
            print("Entrada no válida. Intenta de nuevo.")

def es_primo(x):
    if x <= 1:
        return False
    if x == 2 or x == 3:
        return True
    for i in range(2, x):  # Verifica todos los números desde 2 hasta x-1
        if x % i == 0:
            return False  # Si encuentra un divisor, no es primo
    return True  # Si no encontró divisores, es primo

num = ingresar()
if es_primo(num):
    print("Es primo")
else:
    print("No es primo")

