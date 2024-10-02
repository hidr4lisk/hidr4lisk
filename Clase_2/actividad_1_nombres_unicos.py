#Actividad 1 - Nombres únicos
#Crea un programa que solicite al usuario ingresar nombres separados por comas. Luego, crea un conjunto con los nombres ingresados y muestra por pantalla la cantidad de nombres únicos en el conjunto.

#ingreso:

nombres = input("Ingrese los nombres separados por \",\": ")
print(nombres)

#crear conjunto:

lista_de_nombres = nombres.split(",") #con split arma la lista
lista_de_nombres = set(lista_de_nombres) #para sacar los repetidos
print(lista_de_nombres)