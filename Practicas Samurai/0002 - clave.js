//Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.
let clave = 0
while (clave === 0) {
    clave = prompt('ingrese una clave: ')
    alert(`La clave es: ${clave}`)
}
ingreso = prompt("Ingrese la clave para entrar: ")
if (ingreso.toLowerCase() === clave.toLowerCase()){
    alert("Contraseña correcta")
} else {
    alert("Contraseña incorrecta")
}