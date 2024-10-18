//Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.

let edad = -1
while (edad < 0 || isNaN(edad)) {
    edad = Number(prompt('Ingrese una edad válida: '))
}

if (edad >= 18) {
    alert('Es mayor de edad')
} else {
    alert('No es mayor de edad')
}
