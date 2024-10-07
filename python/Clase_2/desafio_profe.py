#Crea dos listas lista_1 y lista_2, con cualquier elemento que quieras. Realiza los siguientes puntos usando las funciones integradas ya vistas y el método slice [ : ] Imprime la lista correspondiente luego de cada punto.

lista1 = []
lista2 = []

#Añade a la lista_1 el <int> 456789 y luego el <str> "Hola Mundo"

lista1.append(456789)
lista1.append("Hola Mundo")

#Luego añade a la lista_2 el <str> "Hola y adiós", y luego el <int> 5555

lista2.append("Hola y adiós")
lista2.append(5555)

#Genera una lista_3 con todos los elementos de la lista_1 sin considerar el último elemento [:]

lista3 = lista1[:-1]

#Genera una lista_4 con todos los elementos de la lista_2 menos el primero y el último elemento [:]

lista4 = lista2[1:-1]

#Finalmente, genera una lista_5 con los elementos de la lista_4 y de la lista_3

lista5 = lista4 + lista3

print(f" lista_1: {lista1},\n lista_2: {lista2},\n lista_3: {lista3},\n lista_4: {lista2},\n lista_5: {lista5}")