//Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.
let palabra = prompt("Ingrese la palabra que quiere repetir: ")
for (i=0;i<10;i++){
    console.log(`${palabra} ${i}`)
}