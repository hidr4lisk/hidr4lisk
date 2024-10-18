"""

A partir del siguiente diccionario:

numeros = {"uno": 1, "dos": 2, "tres": 3, "cuatro": 4}

a) Preguntar al usuario que introduzca una clave del diccionario.

Si existe, mostrar un mensaje que diga que se ha encontrado, en caso contrario, que no.

b) Preguntar al usuario que introduzca un valor del diccionario.

Si existe, mostrar un mensaje que diga que se ha encontrado, en caso contrario, que no.

"""
numeros = {"uno": 1, "dos": 2, "tres": 3, "cuatro": 4}

# A -------

pregunta = input("Ingresé una clave del diccionario: ")

if pregunta in numeros.keys():
  print("Si existe")
else:
  print("No existe")

# B -------

pregunta2 = input("Ingresé un valor del diccionario:  ")

if pregunta2 in numeros.values():
  print("Si existe")
else:
  print("No existe")
>>>>>>> b80303ea8feb9c45398b098622395a52c1875c1c
