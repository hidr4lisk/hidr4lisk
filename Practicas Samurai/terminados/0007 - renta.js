//Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:
//Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le corresponde.
//rangos = (0,10000),(10000,20000),(20000,35000),(35000,60000),(60000)
let renta = Number(prompt("Ingrese su renta: "))
let impuesto = 0
if (renta < 0 && renta<10000) {
    impuesto = 5
} else if (renta < 20000){
    impuesto = 15
} else if (renta < 35000){
    impuesto = 20
} else if (renta < 60000){
    impuesto = 30
} else {
    impuesto = 45
}

let conImpuestos = renta + ((renta * impuesto)/100)
alert (`Su renta es ${renta} y el valor de impuesto que le corresponde es ${impuesto}%`)
alert (`Con impuestos queda en ${conImpuestos}`)