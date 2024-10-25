def saludar_con_nombre(nombre):  # nombre es un parámetro obligatorio
    print(f"¡Hola {nombre}!")

usuario = input("Ingrese su nombre: ")
saludar_con_nombre(usuario)