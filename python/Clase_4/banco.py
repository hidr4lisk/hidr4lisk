#Una empresa debe aprobar o no un crédito para un cliente.
#Las condiciones son las siguientes:
#    - El cliente debe ser mayor de edad.
#    - Debe tener una antigüedad en el sistema financiero mínimo de 3 años
#    y un ingreso mayor a 2500 dólares.
#    - En caso de que no tenga la antigüedad suficiente,
#    su ingreso mensual debe ser como mínimo 4000 dólares.
#Si no cumple ninguna de las condiciones, no se aprueba el crédito.

#Ingreso del cliente:
edad = int(input("Ingrese la edad del cliente en números: "))
antiguedad = int(input("Ingrese la antiguedad del cliente expresado en años: "))
ingreso_mensual = int(input("Ingrese los ingresos mensuales del cliente en números: "))

#Verificación de condiciones:
if edad >= 18:
    if antiguedad >= 3 and ingreso_mensual > 2500:
        print("El crédito ha sido aprobado.")
    elif antiguedad < 3 and ingreso_mensual >= 4000:
        print("El crédito ha sido aprobado.")
    else:
        print("El crédito no ha sido aprobado.")
else:
    print("No aplican menores de Edad, retirese del establecimiento.")

