//Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 12 años debe pagar 5€, si tiene entre 13 y 17 debe pagar 8€ y si es mayor de 18 años, 10€.

// Preguntamos edad al cliente
let edad = Number(prompt("Ingrese su edad: "))
// Calculamos por edad el precio
if (edad < 4){
    alert("Entra gratis")
} else if (edad >= 4 && edad <= 12){
    alert("Paga $5")
} else if (edad >12 && edad < 18){
    alert("Paga $8")
} else{
    alert("Paga $10")
}