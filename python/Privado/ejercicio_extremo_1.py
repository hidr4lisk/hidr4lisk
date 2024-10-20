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
    try:
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
            eliminar_libro = input("Ingrese el título del libro que desea eliminar: ")
            if eliminar_libro in biblioteca:
                del biblioteca[eliminar_libro]
                print(f"El libro '{eliminar_libro}' ha sido eliminado.")
            else:
                print("Libro no encontrado en la biblioteca.")
        elif opcion == 4:
            if biblioteca:
                print("Lista de libros en la biblioteca:")
                for titulo, autor in biblioteca.items():
                    print(f"Título: {titulo}, Autor: {autor}")
            else:
                print("No hay libros en la biblioteca.")
        elif opcion == 5:
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, elija una opción del 1 al 5.")
    except ValueError:
        print("Opción no válida. Por favor, elija una opción del 1 al 5.")