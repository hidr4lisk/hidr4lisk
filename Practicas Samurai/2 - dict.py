"""
Dado el siguiente diccionario:
Eliminar el contenido de la clave 'Alemania' y mostrar el diccionario resultante
"""
paises = {
    "Canadá": {"capital": "Ottawa", "habitantes": 1015400},
    "Alemania": {"capital": "Berlín", "habitantes": 3644826},
}
paises["Alemania"]={}
print(paises)