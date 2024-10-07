#Ejercicio 6.5. Escribir una función que dada una cadena de caracteres, devuelva:
#    a) La primera letra de cada palabra. Por ejemplo, si recibe 'Universal Serial Bus' debe
#        devolver 'USB'.
#    b) Dicha cadena con la primera letra de cada palabra en mayúsculas. Por ejemplo, si recibe
#        'república argentina' debe devolver 'República Argentina'.
#    c) Las palabras que comiencen con la letra `A'. Por ejemplo, si recibe 'Antes de ayer'
#        debe devolver 'Antes ayer'


cadena_1 = "Python es un lenguaje de programación"
cadena_2 = "asociación de cooperativas"
cadena_3 = "Ayer y hoy todos Actuaron juntos"

eleccion = 0
while eleccion <1 or eleccion >3:
     eleccion = int(input("Elija 1, 2 o 3: "))

if eleccion == 3:
    cadena_elegida = cadena_3
elif eleccion == 2:
    cadena_elegida = cadena_2
else:
    cadena_elegida = cadena_1

iniciales = "".join([palabra[0].upper() for palabra in cadena_elegida.split()])

print(f"\nUsted eligió la Cadena {eleccion}: \" {cadena_elegida}\n\n\"Sus iniciales son\"{iniciales}\"\n")

mayus_primera_letra = " ".join([palabra[0].upper()+palabra[1:] for palabra in cadena_elegida.split()])
print(f"Mayúscula la primera letra: \"{mayus_primera_letra}\"\n")

solo_empieza_con_a = " ".join([palabra for palabra in cadena_elegida.split() if palabra[0].upper() == "A"])
print(f"Solo palabras con \"A\": \"{solo_empieza_con_a}\"\n")