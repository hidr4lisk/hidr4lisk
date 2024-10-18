//Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.

//ingreso del usuario
let numero;
let lista = [];
// Pedir al usuario un número entero positivo
do {
    numero = Number(prompt("Ingrese un número entero positivo:"));
} while (isNaN(numero) || numero < 1 || !Number.isInteger(numero));
// Generar la cuenta atrás y almacenarla en la lista
for (let i = numero; i >= 0; i--) {
    lista.push(i);
}
// Mostrar la lista separada por comas
alert(lista.join(", "));