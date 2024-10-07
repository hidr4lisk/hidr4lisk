cadena_1 = "anita lava la tina"
cadena_2 = "python programming"
cadena_3 = "a man a plan a canal panama"
vocales = ["a", "e", "i", "o", "u"]

eleccion = 0
while eleccion < 1 or eleccion > 3:
    eleccion = int(input("Elija 1, 2 o 3: "))

if eleccion == 3:   cadena_elegida = cadena_3
elif eleccion == 2: cadena_elegida = cadena_2
else:   cadena_elegida = cadena_1

# a) Devuelva solamente las letras consonantes (manteniendo los espacios)
solo_consonantes = ""
for letra in cadena_elegida:
    if letra.lower() not in vocales and letra.isalpha():
        solo_consonantes += letra
    elif letra == " ":
        solo_consonantes += " "  # Mantiene los espacios

print(f"\nUsted eligió la Cadena {eleccion}: \"{cadena_elegida}\"\n")
print(f"Solo consonantes: {solo_consonantes}\n")

# b) Devuelva solamente las letras vocales (manteniendo los espacios)
solo_vocales = ""
for letra in cadena_elegida:
    if letra.lower() in vocales:
        solo_vocales += letra
    elif letra == " ":
        solo_vocales += " "  # Mantiene los espacios

print(f"Solo vocales: {solo_vocales}\n")

# c) Reemplace cada vocal por su siguiente vocal
reemplazado_vocales = ""
for letra in cadena_elegida:
    if letra.lower() in vocales:
        index_vocal = vocales.index(letra.lower())
        if index_vocal == len(vocales) - 1:  # Si es la última vocal ('u'), la reemplaza por 'a'
            reemplazado_vocales += vocales[0]
        else:
            reemplazado_vocales += vocales[index_vocal + 1]
    else:
        reemplazado_vocales += letra  # Si no es vocal, la deja tal cual

print(f"Reemplazando vocales: {reemplazado_vocales}\n")

# d) Indique si se trata de un palíndromo (eliminando espacios para la verificación)
cadena_sin_espacios = cadena_elegida.replace(" ", "").lower()  # Remover espacios y pasar a minúsculas
es_palindromo = cadena_sin_espacios == cadena_sin_espacios[::-1]

if es_palindromo:
    print(f"La cadena \"{cadena_elegida}\" es un palíndromo.\n")
else:
    print(f"La cadena \"{cadena_elegida}\" no es un palíndromo.\n")
