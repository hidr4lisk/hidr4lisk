"""
Escribir un programa que lea una cadena de texto del usuario y encuentre las palabras únicas en esa cadena. Para hacerlo, debes seguir los siguientes pasos:
Leer una cadena de texto del usuario usando la función input()
Convertir la cadena de texto en una lista de palabras utilizando la función split()
Convertir la lista de palabras en un conjunto para eliminar las palabras duplicadas con set()
Convertir el conjunto de vuelta en una lista ordenada utilizando la función list() y sort()
Imprimir las palabras únicas en orden alfabético utilizando la función print().
"""
cadena = input("Ingrese una cadena de texto: ")
cadena_lista = cadena.split()
cadena_conjunto = set(cadena_lista)
cadena_lista_filtrada = list(cadena_conjunto)
cadena_lista_filtrada.sort()
print(cadena_lista_filtrada)

