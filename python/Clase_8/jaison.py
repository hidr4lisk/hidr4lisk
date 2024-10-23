import json
from pathlib import Path

BASE_DIR = Path(__file__).parent

nombre = input("Nombre: ")
edad = int(input("Edad: "))
formulario = {"nombre": nombre, "edad": edad}

archivo = open(BASE_DIR / "jaison.json", "w", encoding="utf-8")
json.dump(formulario, archivo, indent=4)