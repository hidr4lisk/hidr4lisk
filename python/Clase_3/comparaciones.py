#🆗 Debes ingresar los datos con input():
nombre = input("Ingrese Nombre: ")
edad = int(input("Ingrese Edad: "))
#nombre sea diferente de cuatro asteriscos ****
condicion_1 = nombre != "****"
#edad sea mayor que 5 y a su vez menor que 20
condicion_2 = edad > 5 and edad < 20
#Que la longitud de nombre sea mayor o igual a 4  pero a la vez menor que 8
condicion_3 = len(nombre) >= 4 and len(nombre) < 8
#edad multiplicada por 3 sea mayor que 35
condicion_4 = edad * 3 > 35
#🚫 No debes usar funciones, condicionales, bucles o cualquier otra instrucción que no hayamos visto
validacion = condicion_1 and condicion_2 and condicion_3 and condicion_4
print(validacion)
