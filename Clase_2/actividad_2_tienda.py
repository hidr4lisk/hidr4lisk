#Actividad 2 - Actualizando la tienda
#Crea un programa que simule un inventario de productos en una tienda. Inicia con un diccionario que contenga algunos productos y sus cantidades. Luego, permite al usuario agregar un nuevo producto con su cantidad y actualizar la cantidad de un producto existente. Muestra el inventario actualizado.

#Productos y cantidades:
#Manzanas => 50
#Bananas => 30
#Peras => 40

inventario = {
    'manzanas': '50',
    'bananas':'30',
    'peras' : '40'
}

print(inventario)

item_nuevo = input("Ingrese el nuevo item: ")
item_n_cant = int(input(f"ingrese la cantidad de {item_nuevo}: "))
inventario[item_nuevo] = item_n_cant

print(inventario)