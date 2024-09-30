#ACTIVIDAD 4 - ¿CUÁNDO Y DÓNDE?
palabras_tupla = ("manzana", "pera", "uva", "naranja", "sandía", "manzana", "plátano", "kiwi", "pera", "fresa", "mango", "uva", "cereza", "manzana", "durazno")
fruta = palabras_tupla[1] #segundo elemento
contar = palabras_tupla.count(fruta) #COUNT cuenta cuantas veces esta en la lista el segundo elemento
print(f"El elemento en segundo lugar es {fruta}\n")
print(f"Ese valor se encuentra {contar} veces.\n")
#Ahora cuantas repeticiones y en que indices
#no utilice palabras_tupla.index(fruta) porque solo devuelve el indice del 1 valor que encuentra y no me gustó
#entonces use este FOR con ENUMERATE
indices = [i for i,f in enumerate(palabras_tupla) if f == fruta]
print(f"En los indices {indices}")