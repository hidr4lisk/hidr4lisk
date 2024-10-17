#Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:
#Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le corresponde.
#rangos = (0,10000),(10000,20000),(20000,35000),(35000,60000),(60000)
renta = int(input("Ingrese su renta: "))
impuesto = 0
if renta < 0 and renta<10000:
    impuesto = 5
elif renta < 20000:
    impuesto = 15
elif renta < 35000:
    impuesto = 20
elif renta < 60000:
    impuesto = 30
else:
    impuesto = 45

conImpuestos = renta + ((renta * impuesto)/100)
print(f"Su renta es {renta} y el valor de impuesto que le corresponde es {impuesto}%")
print(f"Con impuestos queda en {conImpuestos}")