#Actividad 3 - Python uno, Python dos, Python 3...
#Crea un programa que tome una oración ingresada por el usuario y realice las siguientes operaciones: convierte la oración a mayúsculas, cuenta cuántas veces aparece la palabra "python", y muestra la oración sin espacios en blanco al inicio y al final.

#INGRESO DEL USUARIO:
oracion = input("Ingrese una oración: ")
print(oracion.strip()) #elimina los espacios en blanco 

#a Mayúsculas
mayusculas = oracion.upper()
print(mayusculas)

#busca python  ----- Me complique solo
#lista_oracion = oracion.split(" ")
#print(lista_oracion)
#contador = [i for i, f in enumerate(lista_oracion) if f == "python"]
#print(f"\"python\" aparece: {len(contador)} veces")
contador = oracion.count("python")
print(f"\"python\" aparece: {contador} veces")
