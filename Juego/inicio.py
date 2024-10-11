import random

# Barra de puntos que cambia dependiendo de la acción (máximo -10, máximo 10).
barra = 0

# Diccionario que contiene las descripciones de los escenarios para cada nivel.
escenarios = {
    '1': {
        'nivel1_pos': "Estás en la fila del supermercado. Todo parece tranquilo.",

        'nivel2_pos': "En la fila del supermercado, alguien se cuela delante de ti.",

        'nivel3_pos': "La fila del supermercado es un caos, la gente está peleando.",

        'nivel1_neg': "Estás en la fila del supermercado y notas a una persona mayor que parece nerviosa.",

        'nivel2_neg': "En la fila del supermercado, un niño comienza a llorar y nadie lo calma.",
        
        'nivel3_neg': "La situación se ha vuelto tensa, algunos están gritando."
    },
    # Aquí puedes agregar más escenarios...
}

# Función para obtener la opción actual dependiendo del nivel.
def obtener_opcion_actual(barra):
    if -3 <= barra <= 3:
        return 'nivel1_neg' if barra < 0 else 'nivel1_pos'
    elif -6 <= barra <= -4 or 4 <= barra <= 6:
        return 'nivel2_neg' if barra < 0 else 'nivel2_pos'
    elif -9 <= barra <= -7 or 7 <= barra <= 9:
        return 'nivel3_neg' if barra < 0 else 'nivel3_pos'

# Función para realizar la elección.
def elegir_opcion(opcion):
    global barra
    if opcion == 'bueno':
        if barra < 0:
            barra += 1  # Aumenta 1 si es buena y estamos en nivel negativo.
        elif 4 <= barra <= 6 or -6 <= barra <= -4:
            barra += 1  # Aumenta 1 si es buena y estamos en nivel 2.
        elif 7 <= barra <= 9 or -9 <= barra <= -7:
            barra += 1  # Aumenta 1 si es buena y estamos en nivel 3.
    elif opcion == 'malo':
        if barra < 0:
            barra -= 2  # Resta 2 si es mala y estamos en nivel negativo.
        elif 4 <= barra <= 6 or -6 <= barra <= -4:
            barra -= 2  # Resta 2 si es mala y estamos en nivel 2.
        elif 7 <= barra <= 9 or -9 <= barra <= -7:
            barra -= 3  # Resta 3 si es mala y estamos en nivel 3.

# Función principal del juego.
def juego():
    global barra
    while -10 < barra < 10:
        escenario_actual = random.choice(list(escenarios.keys()))
        descripcion = escenarios[escenario_actual][obtener_opcion_actual(barra)]
        print(descripcion)
        decision = input("Elige 'bueno' o 'malo': ").lower()
        elegir_opcion(decision)
        print(f"Barra actual: {barra}")

    if barra <= -10:
        print("Has caído en la maldad extrema. Fin del juego.")
    elif barra >= 10:
        print("Has alcanzado la bondad extrema. Fin del juego.")

# Iniciar el juego.
juego()
