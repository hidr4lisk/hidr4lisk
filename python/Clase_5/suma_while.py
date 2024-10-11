suma = 0
while True:
    ingreso = input("Ingrese el número para sumar o 'exit' para salir : ")
    if ingreso.isdigit() or (ingreso[0] == '-' and ingreso[1:].isdigit()):
        sumador = int(ingreso)
        suma += sumador
        print(f"Suma parcial = {suma}")
    if ingreso == "exit":
        print (f"La suma total fue : {suma}")
        break