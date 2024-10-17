#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capita obtenido en la inversión cada año que dura la inversión.

cantidad = int(input("Ingrese la Cantidad a inverir: "))
intereses = int(input("Ingrese el interes anual: "))
anios = int(input("Ingrese los años de inversión: "))

resultado = cantidad *(1+(intereses /100))**anios
print(f"Con interes de {intereses}% anual, ${cantidad } en {anios} anño/s va a generar un total de ${resultado}")