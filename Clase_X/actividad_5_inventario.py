# Actividad 5 - Inventario con diccionario
# Seguimiento de productos en el inventario.

inventario = {}  # diccionario vacío para almacenar productos y cantidades

while True:
    item = input("Ingrese el item: ")
    cantidad = int(input(f"Ingrese la cantidad de {item}: "))  # aseguramos que la cantidad sea numérica
    
    if item in inventario:  # si el item ya existe en el inventario, actualizamos su cantidad
        inventario[item] += cantidad
    else:
        inventario[item] = cantidad  # si es un nuevo item, lo agregamos
    
    carga = input("Si quiere detenerse escriba 'salir', o presione ENTER para continuar: ")
    if carga.lower() == "salir":
        break

# Mostrar el inventario
print("\nEl inventario está compuesto de:")
for item, cantidad in inventario.items():
    print(f"{item} - {cantidad} unidades")

# Mostrar el total de productos diferentes en el inventario
productos = len(inventario)
print(f"\nHay {productos} productos diferentes en el inventario.")
