"""
A partir de la siguiente lista de invitados:
lista_de_invitados = ["Juan", "María", "Agustina", "Alex", "Catali
Crear una función saludar() para que le diga a cada invitado:
    "¡Bienvenido {nombre}!"
"""
def saludar(nombre):
    print(f"¡Bienvenido {nombre}")


lista_de_invitados = ['Juan', 'María', 'Agustina', 'Alex', 'Catalina']
for i in lista_de_invitados:
    saludar(i)