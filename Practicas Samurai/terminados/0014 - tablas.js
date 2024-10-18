//Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.

for (let i = 1; i <= 10; i++) {
    let linea = ''
    for (let j = 1; j <= 10; j++) {
        linea += `${i * j}\t`
    }
    console.log(linea)
}