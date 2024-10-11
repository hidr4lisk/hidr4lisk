escenarios = {
    "1": [
        {
            "descripcion": "x",
            "pregunta": "x",
            "decison_buena": "x",
            "decison_mala": "x",
            "consecuencia_buena": "x",
            "consecuencia_mala": "x"
        },  # Nivel 1 - cualquier desición buena, suma 1. cualquier desicion mala resta 1 punto.
        {
            "descripcion": "x",
            "pregunta": "x",
            "decison_buena": "x",
            "decison_mala": "x",
            "consecuencia_buena": "x",
            "consecuencia_mala": "x"
        },  # Nivel 2, acá cambia la cosa, si el valor de la barra es NEGATIVO, resta doble. si es Positivo suma doble. 
                {
            "descripcion": "x",
            "pregunta": "x",
            "decison_buena": "x",
            "decison_mala": "x",
            "consecuencia_buena": "x",
            "consecuencia_mala": "x"
        },  # Nivel 3, y aca lo mismo que en nivel 2. Si el valor de la barra es NEGATIVO, resta triple. y si es positivo suma triple.
    ]
}


nivel = 0  #inica en 0, pero se va modificando depende de las elecciones 
escenario_actual = escenarios["1"][nivel]

# Acceder a los valores del escenario
descripcion = escenario_actual["descripcion"]
pregunta = escenario_actual["pregunta"]
decision_buena = escenario_actual["decison_buena"]
decision_mala = escenario_actual["decison_mala"]
consecuencia_buena = escenario_actual["consecuencia_buena"]
consecuencia_mala = escenario_actual["consecuencia_mala"]

# Imprimir los valores
print(descripcion)
print(pregunta)
print(f"Buena decisión: {decision_buena}")
print(f"Mala decisión: {decision_mala}")
