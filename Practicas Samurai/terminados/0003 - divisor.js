//Escribir un programa que pida al usuario dos números y muestre por pantalla su división. 
//Si el divisor es cero el programa debe mostrar un error.

let numeros = []

for (let i = 0; i < 2; i++) {
    let numero
    while (true) {
        if (i === 0) {
            numero = Number(prompt("Ingrese el primer número: "))
        } else {
            numero = Number(prompt("Ingrese el segundo número: "))
        }

        if (!isNaN(numero)) {
            numeros.push(numero)
            break // Salir del bucle si el número es válido
        } else {
            alert("Entrada inválida. Por favor, ingrese un número válido.")
        }
    }
}

// Verificar si el segundo número es cero
if (numeros[1] === 0) {
    alert("No se puede dividir por 0")
} else {
    let resultado = numeros[0] / numeros[1]
    alert(`La división da como resultado ${resultado}`)
}

