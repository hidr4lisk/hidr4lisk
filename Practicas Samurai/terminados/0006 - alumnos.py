#Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.

genero =""
grupo_a_mujer = ["a","b","c","d","e","f","g","h","i","j","k","l"]
grupo_a_hombre = ["ñ","o","p","q","r","s","t","u","v","w","x","y","z"]

# Pedir el nombre del usuario
nombre = input("Ingrese el nombre: ")

# Pedir el genero del usuario
while genero.upper() != "H" and genero.upper() != "M":
    genero = input("Ingrese Genero, <H> hombre o <M> mujer: ")

# Convertir la primera letra del nombre a minúscula para la comparación
primera_letra = nombre[0].lower()

# Verificar si pertenece al grupo A o B
if (genero.upper() == "M" and primera_letra in grupo_a_mujer) or (genero.upper() == "H" and primera_letra in grupo_a_hombre):
    print(f"{nombre} esta en el brupo A")
else:
    print(f"{nombre} esta en el grupo B")