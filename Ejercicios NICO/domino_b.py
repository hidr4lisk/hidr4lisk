def verificacion (fichas):
    ficha_a = [numero for numero in fichas.split()[0] if numero != "-"]
    ficha_b = [numero for numero in fichas.split()[1] if numero != "-"]
    if ficha_a[0] in ficha_b:
        return ("Encajan")
    elif ficha_a[1] in ficha_b:
        return ("Encajan")
    else:
        return ("No Encajan")

def seleccion():
    eleccion = 0
    while eleccion <1 or eleccion >3:
        eleccion = int(input("Elija 1, 2 o 3: "))

    if eleccion == 3:
        return (cadena_3)
    elif eleccion == 2:
        return (cadena_2)
    else:
        return (cadena_1)

cadena_1 = "3-3 4-3"
cadena_2 = "2-2 5-6"
cadena_3 = "1-1 1-5"

cadena_elegida = seleccion() #Elegimos la cadena a utilizar

print(f"Las fichas \"{cadena_elegida}\" {verificacion(cadena_elegida)}")