#Actividad 4 - Alineando la condicional
#Escribe un programa que tome un número entero ingresado por el usuario y muestre "Es positivo" si el número es mayor que cero, de lo contrario, muestra "No es positivo".

num = int(input("Ingrese un numero Entero: "))
resultado = "Es Positivo" if num > 0 else "No es positivo"
print(resultado)