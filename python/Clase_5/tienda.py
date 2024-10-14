# Diccionario de productos y precios
productos = {
    'manzana': 1.5,
    'banana': 1.0,
    'pan': 2.0,
    'leche': 3.0
}

# Lista para almacenar el carrito de compras
carrito = []

print("Bienvenido a la tienda de mercadería.\n")

while True:
    print("Productos disponibles:")
    for producto, precio in productos.items():
        print(f"{producto}: ${precio}")

    # Solicitar al usuario que ingrese un producto
    item = input("\nIngrese el nombre del producto que desea comprar (o 'salir' para finalizar): ").lower()

    # Salir del ciclo si el usuario escribe 'salir'
    if item == 'salir':
        break
    
    # Validar si el producto está en el diccionario
    if item in productos:
        cantidad = int(input(f"¿Cuántas unidades de {item} desea?: "))
        # Agregar al carrito (producto, cantidad)
        carrito.append((item, cantidad))
    else:
        print("El producto no está disponible. Por favor, intente de nuevo.")

# Mostrar el ticket final
print("\n--- TICKET DE COMPRA ---")
total = 0
for item, cantidad in carrito:
    precio = productos[item]
    subtotal = precio * cantidad
    total += subtotal
    print(f"{item} x {cantidad} = ${subtotal:.2f}")

print(f"\nTotal a pagar: ${total:.2f}")
print("\nGracias por su compra.")
