usuarios = [
    {
        'nombre': 'Juan',
        'nacionalidades': ['española', 'francesa', 'italiana'],
    },
    {
        'nombre': 'Jorge',
        'nacionalidades': ['española'],
    },
]

while True:
    buscar = input("Ingrese el nombre a buscar, o escriba 'Salir' para terminar: ").capitalize()
    
    if buscar == "Salir":
        print("Gracias, vuelva pronto!")
        break

    encontrado = False
    for diccionario in usuarios:
        if diccionario["nombre"] == buscar:
            encontrado = True
            print(f"Nacionalidad/es de {buscar}: ")
            for nac in diccionario["nacionalidades"]:
                print(f"  - {nac.capitalize()}")
    
    if not encontrado:
        print(f"El usuario '{buscar}' no ha sido encontrado.")
