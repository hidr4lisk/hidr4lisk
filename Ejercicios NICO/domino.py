def verificacion (ficha_a,ficha_b):
    if ficha_a[0] in ficha_b:
        return ("Encajan")
    elif ficha[1] in ficha_b:
        return ("Encajan")
    else:
        return ("No Encajan")

pares_de_fichas = ((1,1), (2,4)), ((4,1), (8,4)), ((5,1), (1,5))
for ficha in pares_de_fichas:
    print(f"Las fichas {ficha[0]} y {ficha[1]} {verificacion(ficha[0],ficha[1])}")
