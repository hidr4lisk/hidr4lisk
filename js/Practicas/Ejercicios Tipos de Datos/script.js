/*

//1. Escribir un programa que muestre por pantalla la cadena ¡Hola Mundo!.
let nombre = 'Juan'
let apellido = 'Wachosky'
// Imprime: Hola, mi nombre es Juan Wachosky!
console.log(`Hola, mi nombre es ${nombre} ${apellido}!`)


//2. Escribir un programa que almacene la cadena ¡Hola Mundo! en una variable y luego muestre por pantalla el contenido de la variable.
let cadena = '¡Hola Mundo!'
console.log(cadena)


//3. Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla la cadena ¡Hola <nombre>!, donde <nombre> es el nombre que el usuario haya introducido.
let userName = prompt('Escriba su nombre: ')
console.log(`Hola ${userName}!`)


//4. Escribir un programa que muestre por pantalla el resultado de la siguiente operación aritmética
let operacion = ((3+5)/(2*5))**2
console.log(operacion)


//5. Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora.
//Después debe mostrar por pantalla la paga que le corresponde.
let horasTrabajadas =  prompt('Ingrese sus horas trabajadas: ')
let costePorHora = prompt('Ingrese el coste por hora $: ')
let paga = horasTrabajadas * costePorHora
console.log(`Su paga es: $${paga}`)


//6. Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es <imc> 
//donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.
pesoUsuario = Number(prompt('INGRESE su PESO en números: '))
estaturaUsuario = Number(prompt('INGRESE su ALTURA en centimetros: '))
imc = (pesoUsuario / ((estaturaUsuario / 100) ** 2)).toFixed(2)
console.log(`SU IMC ES ${imc}`)


//7. Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> son los números introducidos por el usuario, y <c> y <r> son el cociente y el resto de la división entera respectivamente.

n = Number(prompt("Ingrese el primer número: "))
m = Number(prompt("Ingrese el segundo número: "))
c = n/m
r =n%m
console.log(`La division entre ${n} y ${m} da un cociente ${c} y un resto ${r}`)


//8. Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión.

capitalInvertido =  Number(prompt("Ingrese la cantidad de dinero a invertir: ")) 
interesAnual = (Number(prompt("Ingrese el interes Anual: ")))
anios = Number(prompt("Ingrese los años de inversión: "))
capitalObtenido = capitalInvertido + ((capitalInvertido * interesAnual / 100) * anios);
console.log(`El capital total obtenido en ${anios} años de inversión, con un Interes Anual de %${interesAnual} para un total de $${capitalInvertido} es de :  $${capitalObtenido}`)



//9. Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas.
//Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. 
//Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado.
pesoPayaso = 112
pesoMunieca = 75
cantidadPayasos = Number(prompt("Ingrese la cantidad de Payasos del último pedido: "))
cantidadMuniecas = Number(prompt("Ingrese la cantidad de Muñecas del último pedido: "))
pesoPaquete = (pesoPayaso*cantidadPayasos)+(pesoMunieca*cantidadMuniecas)
console.log(`El paquete a enviar pesa: ${pesoPaquete} gramos.`)




//10. Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste final total.

// Precio habitual de una barra de pan
const precioPorBarra = 3.49;
// Descuento del 60% para pan no fresco
const descuento = 0.6;

// Leer el número de barras vendidas que no son del día
let barrasNoFrescas = parseInt(prompt("Ingrese el número de barras vendidas que no son del día: "));

// Calcular el precio sin descuento
let precioSinDescuento = barrasNoFrescas * precioPorBarra;
// Calcular el descuento total
let descuentoTotal = precioSinDescuento * descuento;
// Calcular el precio final con descuento aplicado
let precioFinal = precioSinDescuento - descuentoTotal;

// Mostrar los resultados
console.log("Precio habitual de una barra de pan: " + precioPorBarra.toFixed(2) + "€");
console.log("Descuento aplicado por no ser fresca: " + (descuento * 100) + "%");
console.log("Coste final total: " + precioFinal.toFixed(2) + "€");

*/

//Solicite al usuario ingresar un número mediante prompt().
//Verifique si el número es par o impar.
//Muestre un mensaje en pantalla utilizando alert() indicando si el número ingresado es par o impar.

let numero = Number(prompt("Ingrese un número :"))
let paridad = numero % 2
if (paridad === 0) {
    alert("Es par");
} else {
    alert("Es impar") } 