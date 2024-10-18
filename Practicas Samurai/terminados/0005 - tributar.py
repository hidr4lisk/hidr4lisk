#Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.

edad = -1
ingresos = -1

while edad < 1:
    try:
        edad = int(input('Ingrese la edad: '))
        if edad < 1:
            print("Por favor, ingrese una edad válida (mayor o igual a 0).")
    except ValueError:
        print("Error, ingreso no válido. Debe ser un número entero.")

while ingresos < 0:
    try:
        ingresos = int(input('Ingresos: '))
        if ingresos < 0:
            print("Por favor, ingrese un valor de ingresos válido (mayor o igual a 0).")
    except ValueError:
        print("Error, ingreso no válido. Debe ser un número entero.")

if edad > 16 and ingresos >= 1000:
    print("Tiene que tributar")
else:
    print("No tiene que tributar")
