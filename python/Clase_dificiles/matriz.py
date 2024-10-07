matriz = [
[1, 5, 1],
[2, 1, 2],
[3, 0, 1],
[1, 4, 4],
]
suma = 0
for i in range(len(matriz)):
    for x in range(len(matriz[i])):
        suma += matriz[i][x]
    matriz[i].append(suma)
    suma=0
print(matriz)