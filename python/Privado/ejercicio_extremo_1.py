# Ejercicio Extremo 1
# Descripción: Crea un programa que gestiona una biblioteca utilizando un diccionario.
# Permite agregar libros, buscar libros por título, eliminar libros y mostrar todos los libros disponibles.

# Instrucciones:
# 1. Crea un diccionario vacío llamado `biblioteca`.
# 2. Ofrece un menú al usuario con las siguientes opciones:
#    - 1: Agregar libro (título y autor)
#    - 2: Buscar libro por título
#    - 3: Eliminar libro
#    - 4: Mostrar todos los libros
#    - 5: Salir

#Biblioteca vacia
biblioteca = {}

#Comienzo del programa y repite hasta usar la opcion SALIR
while True:
    print("\nBiblioteca Personal:")
    print("1. Agregar libro (título y autor)")
    print("2. Buscar libro por título")
    print("3. Eliminar libro")
    print("4. Mostrar todos los libros")
    print("5. Salir")
    opcion = int(input("Seleccione una opción: "))
    
    #Ahora depende de la opcion lo que pase:
    if opcion == 1:
        titulo = input("Ingrese el Título del libro: ")
        autor = input("Ingrese el Autor del libro: ")
        biblioteca[titulo]=autor
        print(biblioteca)
    elif opcion == 2:
        buscar_libro = input("Ingrese el libro a buscar: ")
        if buscar_libro in biblioteca:
            print(f"El libro {buscar_libro} ya se encuentra en la biblioteca")
        else:
            print("Libro no encontrado")
    elif opcion == 3:
        