
# Ejercicio Extremo
# Descripción: Crea un programa que gestiona una agenda de contactos utilizando un diccionario.
# Permite agregar, buscar y eliminar contactos.

# Instrucciones:
# 1. Crea un diccionario vacío llamado `agenda`.
# 2. Ofrece un menú al usuario con las siguientes opciones:
#    - 1: Agregar contacto (nombre y número de teléfono)
#    - 2: Buscar contacto por nombre
#    - 3: Eliminar contacto
#    - 4: Mostrar todos los contactos
#    - 5: Salir

agenda = {}

while True:
    print("\nMenú:")
    print("1. Agregar contacto")
    print("2. Buscar contacto")
    print("3. Eliminar contacto")
    print("4. Mostrar todos los contactos")
    print("5. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Ingrese el nombre: ")
        telefono = input("Ingrese el número de teléfono: ")
        agenda[nombre] = telefono
        print("Contacto agregado.")
    elif opcion == "2":
        nombre = input("Ingrese el nombre a buscar: ")
        if nombre in agenda:
            print(f"Número de teléfono de {nombre}: {agenda[nombre]}")
        else:
            print("Contacto no encontrado.")
    elif opcion == "3":
        nombre = input("Ingrese el nombre a eliminar: ")
        if nombre in agenda:
            del agenda[nombre]
            print("Contacto eliminado.")
        else:
            print("Contacto no encontrado.")
    elif opcion == "4":
        print("Contactos actuales:")
        for nombre, telefono in agenda.items():
            print(f"{nombre}: {telefono}")
    elif opcion == "5":
        print("Adiós.")
        break
    else:
        print("Opción no válida. Intente de nuevo.")
