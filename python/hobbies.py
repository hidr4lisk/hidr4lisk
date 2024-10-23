#Crea un programa que pida por teclado (input) los datos de tus tres hobbies favoritos y los mismos se guarden en un archivo que se llame miHobbieFavorito.txt.
#EXTRA: ¡Hacerlo con un for o un while para no repetir tanto…!
archivo = open("miHobbieFavorito.txt", "w", encoding="UTF-8")
favoritos = []
while True:
    hobbie = input("Ingrese hobbie favorito: ")
    favoritos.append(hobbie)
    if len(favoritos)== 3:
        break
i = 0    
for hobbi_fav in favoritos:
    i+= 1
    archivo.write(f"Hobbie {i}: {hobbi_fav}\n")    
archivo.close()
