//Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capita obtenido en la inversión cada año que dura la inversión.

let cantidad = Number(prompt("Ingrese la Cantidad a invertir: "))
let interes = Number(prompt("Ingrese el interes anual: ")) 
let anios = Number(prompt("Ingrese los años de inversión: "))

let resultado = cantidad * (1 + (interes /100))**anios
alert(`Con interes del ${interes}% anual, ${cantidad} en ${anios}año/s va a generar un total de $${resultado}`)