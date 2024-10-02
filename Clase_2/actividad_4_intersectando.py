#Actividad 4 - Intersectando y uniendo
#Crea dos conjuntos con números ingresados por el usuario y separados por coma. Luego, muestra cuáles elementos tienen en común los conjuntos y crea un nuevo conjunto que contenga la unión de ambos.

#Creando los conjuntos. 
conjunto_a = input("Ingrese los objetos del conjunto A separados por \",\": ").split(",")
conjunto_b = input("Ingrese los objetos del conjunto B separados por \",\": ").split(",")

print(f"Conjunto A: {conjunto_a}")
print(f"Conjunto B: {conjunto_b}")

#aca vemos cuales estan en comun
conjunto_c = [i for i in conjunto_b if i in conjunto_a ]
print(f"Elementos en común: {conjunto_c}")

#aca unimos los conjuntos
unidos = conjunto_a + conjunto_b
print(f"Unidos A y B = {unidos}")