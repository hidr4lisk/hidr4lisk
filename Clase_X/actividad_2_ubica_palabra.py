#Actividad 2 - Ubica la palabra
#Escribe un programa que tome una lista de nombres ingresados por el usuario separados por un espacio y los liste mostrando su ubicacion.
#Aclaraciones----------------------------------------------------------
#Recuerda usar el split para separar un string. También ten presente la funcionalidad enumerate.
#----------------------------------------------------------------------
nombres = input("Ingrese nombres separados por ESPACIO:    ")
lista_nombres = nombres.split(" ")
print(lista_nombres)

# Usando enumerate para obtener el índice y el nombre
for i, nombre in enumerate(lista_nombres, start=1):  
# start=1 para que empiece desde 1
    print(f"Ubicación: {i}, Nombre: {nombre}")
