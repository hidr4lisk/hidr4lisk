"""
Transforma el texto en:
Gordon lanzó su curva...
- Strawberry ha fallado por un pie! -gritó Joe Castiglione.
- Dos pies -le corrigió Troop.
- Strawberry menea la cabeza como disgustado... -agrega el comentarista.
"""
"""
INFO_2 = "gordon lanzó su curva&strawberry ha fallado por un pie! -gritó Joe Castiglione&dos pies -le corrigió Troop&strawberry menea la cabeza como disgustado… -agrega el comentarista&Mike Jhonson se acerca a alentar a su compañero"
"""
original = "gordon lanzó su curva&strawberry ha fallado por un pie! -gritó Joe Castiglione&dos pies -le corrigió Troop&strawberry menea la cabeza como disgustado… -agrega el comentarista&Mike Jhonson se acerca a alentar a su compañero"

lista_frases = original.lower().split("&")
nombres = ["gordon", "strawberry", "joe", "castiglione", "troop", "mike", "jhonson"]

for frase in lista_frases:
    for i in nombres:
        frase = frase.replace(i, i.capitalize())
    print(frase)
