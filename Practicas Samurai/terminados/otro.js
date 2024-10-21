/* Escribir un programa que lea una cadena de texto del usuario y encuentre las palabras únicas en esa cadena. Para hacerlo, debes seguir los siguientes pasos:
Leer una cadena de texto del usuario usando la función input()
Convertir la cadena de texto en una lista de palabras utilizando la función split()
Convertir la lista de palabras en un conjunto para eliminar las palabras duplicadas con set()
Convertir el conjunto de vuelta en una lista ordenada utilizando la función list() y sort()
Imprimir las palabras únicas en orden alfabético utilizando la función print(). */

let cadenaTexto = prompt("Ingrese una cadena de texto: ");
let lista = cadenaTexto.split(" "); // Dividir la cadena en palabras usando espacio como delimitador
let listaSinDuplicados = [...new Set(lista)]; // Convertir el Set en un array utilizando el operador de propagación
listaSinDuplicados.sort(); // Ordenar el array alfabéticamente
alert(listaSinDuplicados); // Mostrar el resultado en una alerta
