def ingresar():
    while True:
        entrada = input("Por favor, ingresa un número: ")
        if entrada.isdigit():  # Verifica si la entrada es un número entero positivo
            return int(entrada)
        else:
            print("Entrada no válida. Intenta de nuevo.")

def año_bisiesto(x):
    if (x % 4 == 0 and x % 100 != 0) or (x % 400 == 0):
        return (True)
    else:
        return(False)
    
bisi = ingresar()
if año_bisiesto(bisi):
    print(f"El año {bisi} es bisiesto.")
else:
    print(f"El año {bisi} no es bisiesto.")