// Función para cargar los datos de los estudiantes
function cargaEstudiantes(num) {
    let estudiantes = []; // Array para almacenar los datos de los estudiantes

    for (let i = 0; i < num; i++) {
        let nombre = prompt("Ingrese el nombre del estudiante:");
        let nota1 = parseFloat(prompt("Ingrese la primera nota:")); // Convertir a número
        let nota2 = parseFloat(prompt("Ingrese la segunda nota:")); // Convertir a número
        let nota3 = parseFloat(prompt("Ingrese la tercera nota:")); // Convertir a número
        let promedio = (nota1 + nota2 + nota3) / 3;
        
        // Agregar un objeto con nombre y promedio al array de estudiantes
        estudiantes.push({ nombre: nombre, promedio: promedio });
    }

    return estudiantes; // Retornar el array de estudiantes
}

// Función para verificar si cada estudiante está aprobado o desaprobado
function verificarAprobacion(estudiantes) {
    let resultados = []; // Array para almacenar los resultados de aprobación

    for (let i = 0; i < estudiantes.length; i++) {
        let estado = estudiantes[i].promedio >= 7 ? "Aprobado" : "Desaprobado"; // Verificar si el promedio es mayor o igual a 7
        // Agregar el nombre del estudiante y su estado (aprobado/desaprobado) al array
        resultados.push({ nombre: estudiantes[i].nombre, estado: estado, promedio: estudiantes[i].promedio });
    }

    return resultados; // Retornar el array con los resultados de aprobación
}

// Programa principal
let cantidad = parseInt(prompt("Ingrese la cantidad de estudiantes total:"));
let estudiantes = cargaEstudiantes(cantidad); // Llamar a la función para cargar estudiantes
let resultadoAprobacion = verificarAprobacion(estudiantes); // Verificar si están aprobados

// Mostrar los resultados de aprobación
console.log("Resultados de aprobación:");
for (let i = 0; i < resultadoAprobacion.length; i++) {
    console.log(`Nombre: ${resultadoAprobacion[i].nombre}, Promedio: ${resultadoAprobacion[i].promedio}, Estado: ${resultadoAprobacion[i].estado}`);
}
