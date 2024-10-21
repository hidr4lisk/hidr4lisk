import json

# Nombre del archivo donde se guardarán las tareas
FILENAME = 'tareas.json'

# Función para cargar las tareas desde el archivo
def cargar_tareas():
    try:
        with open(FILENAME, 'r') as file:
            return json.load(file)  # Cargar las tareas desde el archivo
    except FileNotFoundError:
        return []  # Si el archivo no existe, devolver una lista vacía

# Función para guardar las tareas en el archivo
def guardar_tareas(tareas):
    with open(FILENAME, 'w') as file:
        json.dump(tareas, file, indent=4)  # Guardar las tareas en el archivo

# Función para agregar una nueva tarea
def agregar_tarea(tareas, descripcion):
    tareas.append({"descripcion": descripcion, "completada": False})
    guardar_tareas(tareas)
    print(f"Tarea '{descripcion}' agregada.")

# Función para eliminar una tarea por su índice
def eliminar_tarea(tareas, indice):
    if 0 <= indice < len(tareas):
        tarea_eliminada = tareas.pop(indice)
        guardar_tareas(tareas)
        print(f"Tarea '{tarea_eliminada['descripcion']}' eliminada.")
    else:
        print("Índice inválido.")

# Función para marcar una tarea como completada o pendiente
def marcar_tarea(tareas, indice, completada):
    if 0 <= indice < len(tareas):
        tareas[indice]["completada"] = completada
        guardar_tareas(tareas)
        estado = "completada" if completada else "pendiente"
        print(f"Tarea '{tareas[indice]['descripcion']}' marcada como {estado}.")
    else:
        print("Índice inválido.")

# Función para mostrar todas las tareas
def mostrar_tareas(tareas):
    if not tareas:
        print("No hay tareas.")
        return

    for i, tarea in enumerate(tareas):
        estado = "✔️" if tarea["completada"] else "❌"
        print(f"{i}. {tarea['descripcion']} - {estado}")

# Programa principal
def main():
    tareas = cargar_tareas()  # Cargar tareas al inicio

    while True:
        print("\n--- Menú de Tareas ---")
        print("1. Mostrar tareas")
        print("2. Agregar tarea")
        print("3. Eliminar tarea")
        print("4. Marcar tarea como completada")
        print("5. Marcar tarea como pendiente")
        print("6. Salir")

        opcion = input("Elige una opción: ")

        if opcion == '1':
            mostrar_tareas(tareas)
        elif opcion == '2':
            descripcion = input("Descripción de la tarea: ")
            agregar_tarea(tareas, descripcion)
        elif opcion == '3':
            indice = int(input("Índice de la tarea a eliminar: "))
            eliminar_tarea(tareas, indice)
        elif opcion == '4':
            indice = int(input("Índice de la tarea a marcar como completada: "))
            marcar_tarea(tareas, indice, True)
        elif opcion == '5':
            indice = int(input("Índice de la tarea a marcar como pendiente: "))
            marcar_tarea(tareas, indice, False)
        elif opcion == '6':
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Por favor, elige una opción válida.")

if __name__ == "__main__":
    main()