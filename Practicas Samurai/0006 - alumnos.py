#Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.

nombre = 0
genero = 3
grupo_a_mujer = ["a","b","c","d","e","f","g","h","i","j","k","l"]
grupo_a_hombre = ["ñ","o","p","q","r","s","t","u","v","w","x","y","z"]

while True:
    try:
        nombre = input("Ingrese el nombre: ")
