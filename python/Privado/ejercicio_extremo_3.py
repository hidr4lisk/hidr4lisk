
# Ejercicio Extremo 3
# Descripción: Crea un programa que gestiona una lista de estudiantes y sus calificaciones.
# Permite agregar estudiantes, calcular el promedio de calificaciones y mostrar la lista de estudiantes.

# Instrucciones:
# 1. Crea un diccionario vacío llamado `estudiantes`.
# 2. Ofrece un menú al usuario con las siguientes opciones:
#    - 1: Agregar estudiante (nombre y calificación)
#    - 2: Calcular y mostrar el promedio de calificaciones
#    - 3: Mostrar todos los estudiantes
#    - 4: Salir

# Diccionario vacío para almacenar estudiantes y calificaciones
estudiantes = {}

# Función para mostrar el menú
def mostrar_menu():
    print("\nGestión de Estudiantes:")
    print("1. Agregar estudiante (nombre y calificación)")
    print("2. Calcular y mostrar el promedio de calificaciones")
    print("3. Mostrar todos los estudiantes")
    print("4. Salir")

# Comienzo del programa
while True:
    mostrar_menu()
    
    # Bloque para manejar la selección del menú
    try:
        opcion = int(input("Seleccione una opción: "))
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número del 1 al 4.")
        continue
    
    # Opción 1: Agregar estudiante
    if opcion == 1:
        nombre = input("Ingrese el nombre del estudiante: ")
        
        # Bloque para manejar la entrada de la calificación
        try:
            calificacion = float(input(f"Ingrese la calificación de {nombre}: "))
        except ValueError:
            print("Calificación no válida. Debe ser un número.")
            continue
        
        estudiantes[nombre] = calificacion
        print(f"Estudiante '{nombre}' agregado con calificación {calificacion}.")
    
    # Opción 2: Calcular y mostrar el promedio de calificaciones
    elif opcion == 2:
        if estudiantes:
            promedio = sum(estudiantes.values()) / len(estudiantes)
            print(f"El promedio de las calificaciones es: {promedio:.2f}")
        else:
            print("No hay estudiantes registrados para calcular el promedio.")
    
    # Opción 3: Mostrar todos los estudiantes
    elif opcion == 3:
        if estudiantes:
            print("Lista de estudiantes y sus calificaciones:")
            for nombre, calificacion in estudiantes.items():
                print(f"Estudiante: {nombre}, Calificación: {calificacion:.2f}")
        else:
            print("No hay estudiantes registrados.")
    
    # Opción 4: Salir
    elif opcion == 4:
        print("Saliendo del programa. ¡Hasta luego!")
        break
    
    # Manejo de opción inválida
    else:
        print("Opción no válida. Por favor, elija una opción del 1 al 4.")
