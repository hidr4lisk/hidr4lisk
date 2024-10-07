 #    b) Devuelva solamente las letras vocales. Por ejemplo, si recibe 'sin consonantes' debe
#        devolver 'i ooae'.
#    c) Reemplace cada vocal por su siguiente vocal. Por ejemplo, si recibe 'vestuario' debe
#        devolver 'vistaerou'.
#    d) Indique si se trata de un palíndromo. Por ejemplo, 'anita lava la tina' es un pa-
#        líndromo (se lee igual de izquierda a derecha que de derecha a izquierda).



cadena_1 = "anita lava la tina"
cadena_2 = "python programming"
cadena_3 = "a man a plan a canal panama"

vocales = ["a","e","i","o","u"]


eleccion = 0
while eleccion <1 or eleccion >3:
     eleccion = int(input("Elija 1, 2 o 3: "))

if eleccion == 3:
    cadena_elegida = cadena_3
elif eleccion == 2:
    cadena_elegida = cadena_2
else:
    cadena_elegida = cadena_1

#a) Devuelva solamente las letras consonantes.
solo_consonantes = letras for letras in cadena_elegida if letras != vocales


print(f"\nUsted eligió la Cadena {eleccion}: \"{cadena_elegida}\"\n")
print (solo_consonantes)