//Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.

let edad = -1
let ingresos = -1

while (edad < 0 || isNaN(edad)) {
    edad = Number(prompt('Ingrese una edad válida: '))
}
while (ingresos < 1 || isNaN(ingresos)){
    ingresos = Number(prompt('Ingrese unos ingresos válidos: '))
}

if (edad > 16 && ingresos >= 1000){
    alert("Tiene que tributar")
} else {
    alert("No tienen que tributar")
}