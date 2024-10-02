print("-------------------------------------------")
print("------------⚽--BIENVENIDO--⚽------------")
print("-------------------------------------------")

#Ingresos
ganados =int(input("Ingrese los partidos Ganados: "))*3
empatados =int(input("Ingrese los partidos Empatados: "))
perdidos =int(input("Ingrese los partidos Perdidos: "))

#calculos

puntaje = (ganados+empatados)/20

#mostrar resultados

print(f"\n El equipo obtuvo {puntaje} Puntos")