setup = ["🀄Carta: ","🏷Nombre: ", "⚔Ataque: ","🛡Defensa: ", "❤Vida: ", "📟Tipo: ", "Descripción: "]

mazo_pylords = [
    (
        '0001',
        'Guerrero del sol',
        20,
        15,
        150,
        'Fuego',
        'El Guerrero del Sol es un monstruo feroz y poderoso. Tiene una fuerza y agilidad incomparables.'
    ),
    (
        '0002',
        'Bruja de la noche',
        18,
        12,
        120,
        'noche',
        'La Bruja de la Noche es una bestia terrible y malvada. Tiene una resistencia y inteligencia extraordinarias.'
    )
]

# Imprimir cada carta con su setup
for carta in mazo_pylords:
    for i in range(len(setup)):
        print(f"{setup[i]}{carta[i]}")
    print()  # Salto de línea entre cada carta