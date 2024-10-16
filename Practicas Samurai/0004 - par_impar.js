//Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.
let numero = "a"
while (numero < 0 || isNaN(numero)) {
    numero = Number(prompt('Ingrese una edad válida: '))
}
let paridad = numero % 2
if (paridad !== 0){
    alert("No es par")
} else {
    alert("es par")
}