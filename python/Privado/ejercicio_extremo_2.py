
# Ejercicio Extremo 2
# Descripción: Crea un programa que simula una lista de compras.
# Permite al usuario agregar, eliminar y mostrar los artículos en la lista.
# Además, calcula el costo total de los artículos ingresados.

# Instrucciones:
# 1. Crea una lista vacía llamada `lista_compras`.
# 2. Ofrece un menú al usuario con las siguientes opciones:
#    - 1: Agregar artículo (nombre y precio)
#    - 2: Eliminar artículo
#    - 3: Mostrar lista de compras
#    - 4: Mostrar costo total
#    - 5: Salir

# Lista de compras vacía
lista_compras = []

# Función para mostrar el menú
def mostrar_menu():
    print("\nLista de Compras:")
    print("1. Agregar artículo (nombre y precio)")
    print("2. Eliminar artículo")
    print("3. Mostrar lista de compras")
    print("4. Mostrar costo total")
    print("5. Salir")

# Comienzo del programa
while True:
    mostrar_menu()
    
    # Bloque para manejar la selección del menú
    try:
        opcion = int(input("Seleccione una opción: "))
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número del 1 al 5.")
        continue
    
    # Opción 1: Agregar artículo
    if opcion == 1:
        nombre = input("Ingrese el nombre del artículo: ")
        
        # Bloque para manejar la entrada del precio
        try:
            precio = float(input("Ingrese el precio del artículo: "))
        except ValueError:
            print("Precio no válido. Debe ser un número.")
            continue
        
        lista_compras.append((nombre, precio))
        print(f"Artículo '{nombre}' agregado a la lista.")

    # Opción 2: Eliminar artículo
    elif opcion == 2:
        eliminar_articulo = input("Ingrese el nombre del artículo que desea eliminar: ")
        for articulo in lista_compras:
            if articulo[0] == eliminar_articulo:
                lista_compras.remove(articulo)
                print(f"Artículo '{eliminar_articulo}' eliminado de la lista.")
                break
        else:
            print("Artículo no encontrado en la lista.")
    
    # Opción 3: Mostrar lista de compras
    elif opcion == 3:
        if lista_compras:
            print("Lista de compras:")
            for articulo in lista_compras:
                print(f"Artículo: {articulo[0]}, Precio: ${articulo[1]:.2f}")
        else:
            print("La lista de compras está vacía.")
    
    # Opción 4: Mostrar costo total
    elif opcion == 4:
        costo_total = sum(articulo[1] for articulo in lista_compras)
        print(f"El costo total de los artículos es: ${costo_total:.2f}")
    
    # Opción 5: Salir
    elif opcion == 5:
        print("Saliendo del programa. ¡Hasta luego!")
        break
    
    # Manejo de opción inválida
    else:
        print("Opción no válida. Por favor, elija una opción del 1 al 5.")
