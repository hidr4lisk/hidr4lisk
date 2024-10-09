# Generaciones Digitales, Validas:
generacion_silenciosa = (1920, 1940)
baby_boomer = (1946, 1964)
generacion_x = (1965, 1979)
generacion_y = (1980, 2000)
generacion_z = (2001, 2010)

# Ingreso del usuario:
año_de_nacimiento = int(input("Ingrese su año de nacimiento: "))

# Ahora comparamos:
if generacion_silenciosa[0] <= año_de_nacimiento <= generacion_silenciosa[1]:
    print("Pertenece a la Generación Silenciosa")
elif baby_boomer[0] <= año_de_nacimiento <= baby_boomer[1]:
    print("Pertenece a la Generación Baby Boomer")
elif generacion_x[0] <= año_de_nacimiento <= generacion_x[1]:
    print("Pertenece a la Generación X")
elif generacion_y[0] <= año_de_nacimiento <= generacion_y[1]:
    print("Pertenece a la Generación Y")
elif generacion_z[0] <= año_de_nacimiento <= generacion_z[1]:
    print("Pertenece a la Generación Z")
else:
    print("No pertenece a la Generación Digital.")
