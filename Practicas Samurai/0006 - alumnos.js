let nombre = "";
let genero = 0;
let grupo_a_mujer = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l"];
let grupo_a_hombre = ["ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"];

// Pedir el nombre del usuario
while (!isNaN(nombre) || nombre.trim() === "") {
    nombre = prompt("Ingrese su nombre: ");
}

// Pedir el género del usuario
while (isNaN(genero) || genero < 1 || genero > 2) {
    genero = Number(prompt("Ingrese su género: 1 para Hombre, 2 para Mujer"));
}

// Convertir la primera letra del nombre a minúscula para la comparación
let primeraLetra = nombre[0].toLowerCase();

// Verificar si pertenece al grupo A o B
if (
    (genero === 2 && grupo_a_mujer.includes(primeraLetra)) || // Mujeres con nombre anterior a la M
    (genero === 1 && grupo_a_hombre.includes(primeraLetra))   // Hombres con nombre posterior a la N
) {
    alert(`${nombre} pertenece al Grupo A`);
} else {
    alert(`${nombre} pertenece al Grupo B`);
}
