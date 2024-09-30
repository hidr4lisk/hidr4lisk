# Introduccion a Strings y Numeros en Python

# 1. STRINGS

# Un string es una cadena de caracteres, como texto. Se define usando comillas simples o dobles.
texto = "Hola Mundo"

# Metodos comunes de strings:

# split(): Divide el string en una lista de palabras usando un separador (por defecto es el espacio).
texto = "Hola, como estas?"
palabras = texto.split()  # ['Hola,', 'como', 'estas?']

# index(): Devuelve la posicion del primer caracter encontrado.
texto = "Python"
posicion = texto.index("t")  # 2

# upper() y lower(): Convierte el string a mayusculas o minusculas.
texto = "Hola"
mayusculas = texto.upper()  # "HOLA"
minusculas = texto.lower()  # "hola"

# replace(): Reemplaza una parte del string por otra.
texto = "Hola Mundo"
nuevo_texto = texto.replace("Mundo", "Python")  # "Hola Python"

# strip(): Elimina los espacios en blanco al principio y al final del string.
texto_strip = "  hola  ".strip()  # 'hola'

# title(): Convierte el primer caracter de cada palabra en mayuscula y el resto en minusculas.
texto = "hola mundo"
titulo = texto.title()  # "Hola Mundo"

# capitalize(): Convierte solo el primer caracter del string en mayuscula y el resto en minusculas.
texto = "hola mundo"
capitalizado = texto.capitalize()  # "Hola mundo"

# casefold(): Convierte el string completamente a minusculas, similar a lower() pero mas agresivo para compatibilidad con alfabetos internacionales.
texto = "ß"
casefolded = texto.casefold()  # "ss"

# count(): Es un metodo de string que cuenta cuantas veces aparece una subcadena especifica en el string.
palabra = "banana"
print(palabra.count("a"))  # Salida: 3

# len(): Devuelve la longitud de una cadena.
longitud = len("Hola mundo")
print(longitud)

# isdigit(): Verifica si todos los caracteres son digitos.
"123".isdigit()  # True

# isalpha(): Verifica si todos los caracteres son letras.
"abc".isalpha()  # True

# startswith(prefix): Verifica si el string comienza con la subcadena especificada.
"python".startswith("py")  # True

# endswith(suffix): Verifica si el string termina con la subcadena especificada.
"python".endswith("on")  # True

# Slices de strings:
# Los slices te permiten extraer partes de un string usando indices.

# Cortar un string:
texto = "Hola Mundo"
saludo = texto[0:4]  # "Hola"

# Invertir un string:
texto = "Python"
invertido = texto[::-1]  # "nohtyP"

# Extraer caracteres especificos:
texto = "abcdef"
parte = texto[1:5:2]  # "bd"


# 2. TIPOS NUMeRICOS

# int (enteros): Numeros sin decimales.
numero = 42

# float (flotantes): Numeros con decimales.
numero = 3.14

# Operaciones basicas con numeros:
# Suma: +
# Resta: -
# Multiplicacion: *
# Division: /
# Division entera: //
# Potencia: **

# Ejemplo de operaciones:
suma = 5 + 3  # 8
division = 7 / 2  # 3.5
potencia = 2**3  # 8

# Conversion entre tipos:
# Para convertir entre tipos numericos, se pueden usar funciones como int() y float().
numero = 3.14
entero = int(numero)  # 3
flotante = float(5)  # 5.0
