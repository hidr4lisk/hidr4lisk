username = "jorge"
password = "banana"

ingreso_user = input("Ingrese su Nombre de Usuario: ")
ingreso_pass = input("Ingrese su Contraseña: ")

if ingreso_user == username and ingreso_pass == password:
    print(f"Hola {username}")
    exit()
else:
    print("Error")