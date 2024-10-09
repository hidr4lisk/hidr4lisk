edad = int(input("Edad: "))
if edad < 13:
    print("Eres niño")
elif edad >= 13 and edad < 18:
    print("Eres adolescente")
elif edad >= 18 and edad < 30:
    print("Eres joven")
elif edad >= 30 and edad < 65:
    print("Eres adulto")
else:
    print("Eres adulto mayor")