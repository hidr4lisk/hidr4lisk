"""
Dada la siguiente lista de usuarios, preguntar qué nombre de usuario desea buscar.
Si es encontrado, mostrar sus nacionalidades iterando con for.
Repetir de forma indeterminada el procedimiento anterior, hasta que el usuario escriba 'salir'
"""
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
    buscar = input("Ingrese el nombre a buscar, o escriba 'salir' para terminar: ")
    for diccionarios in usuarios:
        comparar = diccionarios["nombre"]
        if comparar == buscar.capitalize():
            print(diccionarios.get("nacionalidades"))