
# Ejercicio Normal
# Descripción: Crea un programa que gestione una lista de tareas.
# Permite al usuario agregar tareas, eliminar tareas y mostrar la lista actual de tareas.

# Instrucciones:
# 1. Crea una lista vacía llamada `tareas`.
# 2. Ofrece un menú al usuario con las siguientes opciones:
#    - 1: Agregar tarea
#    - 2: Eliminar tarea
#    - 3: Mostrar tareas
#    - 4: Salir

tareas = []

while True:
    print("\nMenú:")
    print("1. Agregar tarea")
    print("2. Eliminar tarea")
    print("3. Mostrar tareas")
    print("4. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        tarea = input("Ingrese la tarea: ")
        tareas.append(tarea)
        print("Tarea agregada.")
    elif opcion == "2":
        tarea = input("Ingrese la tarea a eliminar: ")
        if tarea in tareas:
            tareas.remove(tarea)
            print("Tarea eliminada.")
        else:
            print("La tarea no se encuentra en la lista.")
    elif opcion == "3":
        print("Tareas actuales:")
        for i, tarea in enumerate(tareas, start=1):
            print(f"{i}. {tarea}")
    elif opcion == "4":
        print("Adiós.")
        break
    else:
        print("Opción no válida. Intente de nuevo.")
