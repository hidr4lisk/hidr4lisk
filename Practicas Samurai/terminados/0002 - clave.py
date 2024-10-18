
#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.

clave = 0

while (clave == 0) :
    clave = input('ingrese una clave: ')
    print(f'La clave es: {clave}')

ingreso = input('Ingrese la clave para entrar: ')

if ingreso.lower() == clave.lower():
    print('Contraseña correcta')
else: 
    print('Contraseña incorrecta')
