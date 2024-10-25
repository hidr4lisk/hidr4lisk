def sumar(a, b):
    return (a + b)

def restar(a, b):
    return (a - b)

def multiplicar(a, b):
    return (a * b)

def dividir(a, b):
    return (a / b)

funciones = [sumar, restar, multiplicar, dividir]
for funcion in funciones:
    print(funcion(2, 3))

