
def ingresar(tipo_partido):
    while True:
        entrada = input(f"Por favor, ingresa la cantidad de partidos {tipo_partido}: ")
        if entrada.isdigit() and int(entrada) >= 0:  # Verifica si la entrada es un número entero mayor o igual a 0
            return int(entrada)
        else:
            print("Entrada no válida. Intenta de nuevo.")
            
ganados = ingresar("ganados")
empatados = ingresar("empatados")
perdidos = ingresar("perdidos")

# Verificación de que la suma no exceda 20
while ganados + empatados + perdidos > 20:
    print("La suma de partidos ganados, empatados y perdidos no puede superar 20. Intenta de nuevo.")
    ganados = ingresar("ganados")
    empatados = ingresar("empatados")
    perdidos = ingresar("perdidos")

puntaje = (ganados * 3 + empatados) / 20
print("El equipo logró un puntaje de: " + str(puntaje))
