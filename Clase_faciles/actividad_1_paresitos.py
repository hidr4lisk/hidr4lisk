#Actividad 1 - Paresitos
#Crea un programa que solicite dos números enteros al usuario y determine si ambos son números pares.

#primero le pedimos al usuario 2 numeros:
numero_uno = int(input("Ingrese el primer número: "))
numero_dos = int(input("Ingrese el segundo número: "))

#ahora a ver si son pares:
prueba_uno = numero_uno % 2
prueba_dos = numero_dos % 2
if prueba_uno == 0:
    paridad_uno = "Es par"
else:
    paridad_uno = "Es impar"
if prueba_dos == 0:
    paridad_dos = "Es par"
else:
    paridad_dos= "Es impar"

print(f"el número {numero_uno} {paridad_uno} y el número {numero_dos} {paridad_dos}")