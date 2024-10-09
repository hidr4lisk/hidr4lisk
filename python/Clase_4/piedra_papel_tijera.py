import random

# Lista de opciones válidas en el juego
opciones_disponibles = ("piedra", "papel", "tijera")

# Función para obtener la elección del jugador
def obtener_eleccion_jugador():
    while True:
        eleccion_jugador = input("Piedra, Papel o Tijera\nElija (o escriba 'salir' para terminar): ").lower()
        if eleccion_jugador.lower() == "salir":
            return "salir"
        elif eleccion_jugador not in opciones_disponibles:
            print("Opción inválida. Intente de nuevo.")
        else:
            return eleccion_jugador

# Función para determinar el resultado del juego
def determinar_resultado(eleccion_jugador, eleccion_maquina):
    if eleccion_jugador == eleccion_maquina:
        print("Empate!")
    elif (eleccion_jugador == "piedra" and eleccion_maquina == "tijera") or \
         (eleccion_jugador == "papel" and eleccion_maquina == "piedra") or \
         (eleccion_jugador == "tijera" and eleccion_maquina == "papel"):
        print("Ganaste!")
    else:
        print("Perdiste!")

# Bucle principal del juego
while True:
    # Obtenemos la elección del jugador
    eleccion_jugador = obtener_eleccion_jugador()

    # Verificamos si el jugador quiere salir
    if eleccion_jugador == "salir":
        print("Gracias por jugar. ¡Adiós!")
        break
    
    # La máquina elige al azar
    eleccion_maquina = random.choice(opciones_disponibles)
    
    # Mostramos las elecciones
    print(f"Tu elección: {eleccion_jugador.upper()}, Máquina: {eleccion_maquina.upper()}")
    
    # Determinamos el resultado
    determinar_resultado(eleccion_jugador, eleccion_maquina)
