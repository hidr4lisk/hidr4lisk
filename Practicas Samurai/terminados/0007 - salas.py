# Rangos >4 gratis / 4 y 12 5$ / 13 y 17 $8 / >18 $10

# Preguntamos edad al cliente
edad = int(input("Ingrese su edad: "))
# Calculamos por edad el precio
if edad < 4:
    print("Entra Gratis")
elif edad >=4 and edad <= 12:
    print("Paga $5")
elif edad >12 and edad <18:
    print("Paga $8")
else:
    print("Paga $10")