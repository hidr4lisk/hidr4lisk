#Actividad 4 - Salteando palabras
#Escribe un programa que tome una lista de palabras ingresadas por el usuario. Luego, que muestre cada palabra una por una. Si la palabra es "salir", finaliza el programa. Si la palabra es "omitir", se pasa a la siguiente iteración. Al final, si ninguna palabra fue "salir", muestra un mensaje avisando la situación.

#Aclaraciones
#Recuerda usar slice para cortar un string.
# Actividad 4 - Salteando palabras
# Escribe un programa que tome una lista de palabras ingresadas por el usuario.

while True:
    listado = input("Ingrese su listado de palabras: ").split(" ")
    for palabra in listado:
        if palabra.lower() == "salir":
            print("Se ha salido del programa.")
            break  # Salimos del bucle for si encontramos "salir"
        if palabra.lower() == "omitir":
            continue  # Pasamos a la siguiente iteración si la palabra es "omitir"
        print(palabra)
    else:
        print("No hay palabra SALIR")  # Este mensaje se mostrará si no se encontró "salir"

    if "salir" in listado:
        break  # Salimos del bucle while si "salir" está en el listado
