def son_multiplos(a, b):
    # Verificamos si a es múltiplo de b y si b es múltiplo de a
    if a % b == 0 or b % a == 0:
        return True
    else:
        return False

# Probá la función
num1 = 10
num2 = 5

if son_multiplos(num1, num2):
    print(f"{num1} y {num2} son múltiplos entre sí.")
else:
    print(f"{num1} y {num2} no son múltiplos entre sí.")
