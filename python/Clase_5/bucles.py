intento = 1
while intento <= 3:
    respuesta = input("Escribe SI: ")
    if respuesta == "SI":
        print("Saliste del programa en el intento", intento)
        quit()
    intento += 1
else:
    print("Has agotado tus tres intentos")