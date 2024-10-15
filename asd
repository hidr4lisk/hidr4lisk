<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cifrar/Descifrar Texto</title>
</head>
<body>
    <h1>Cifrado de Archivos de Texto</h1>

    <label for="action">Elige una opción:</label>
    <select id="action">
        <option value="1">Cifrar</option>
        <option value="2">Descifrar</option>
    </select>
    <br><br>

    <label for="fileInput">Selecciona el archivo de texto:</label>
    <input type="file" id="fileInput" accept=".txt">
    <br><br>

    <button onclick="procesarArchivo()">Procesar</button>

    <script>
        function desplazarCaracteres(texto, x, cifrar = true) {
            let textoProcesado = '';
            for (let i = 0; i < texto.length; i++) {
                let caracter = texto[i];
                if (/[a-zA-Z]/.test(caracter)) {
                    let base = caracter === caracter.toUpperCase() ? 65 : 97;
                    let desplazamiento = (caracter.charCodeAt(0) - base + (cifrar ? x : -x)) % 26;
                    if (desplazamiento < 0) desplazamiento += 26;
                    textoProcesado += String.fromCharCode(base + desplazamiento);
                } else {
                    textoProcesado += caracter;
                }
            }
            return textoProcesado;
        }

        function procesarArchivo() {
            const fileInput = document.getElementById('fileInput');
            const action = document.getElementById('action').value;

            if (!fileInput.files.length) {
                alert('Por favor, selecciona un archivo de texto.');
                return;
            }

            const file = fileInput.files[0];
            const reader = new FileReader();

            reader.onload = function(event) {
                const contenido = event.target.result;
                
                if (action === '1') {  // Cifrar
                    const desplazamiento = Math.floor(Math.random() * 200) - 100; // Genera un número aleatorio entre -100 y 100
                    const resultadoTexto = desplazarCaracteres(contenido, desplazamiento, true);
                    const nombreArchivoSalida = `Readm3 (${desplazamiento}).txt`;
                    descargarArchivo(resultadoTexto, nombreArchivoSalida);
                } else if (action === '2') {  // Descifrar
                    const nombreArchivo = file.name;
                    const regex = /Readm3 \((\-?\d+)\)\.txt/;
                    const coincidencia = nombreArchivo.match(regex);
                    
                    if (!coincidencia) {
                        alert("El nombre del archivo no tiene el formato adecuado. Debe ser 'Readm3 (X).txt', donde X es el desplazamiento.");
                        return;
                    }

                    const desplazamiento = parseInt(coincidencia[1]);
                    const resultadoTexto = desplazarCaracteres(contenido, desplazamiento, false);
                    descargarArchivo(resultadoTexto, 'm3Read.txt');
                }
            };

            reader.readAsText(file);
        }

        function descargarArchivo(contenido, nombreArchivo) {
            const blob = new Blob([contenido], { type: 'text/plain' });
            const enlaceDescarga = document.createElement('a');
            enlaceDescarga.href = URL.createObjectURL(blob);
            enlaceDescarga.download = nombreArchivo;
            document.body.appendChild(enlaceDescarga);
            enlaceDescarga.click();
            document.body.removeChild(enlaceDescarga);
        }
    </script>
</body>
</html>
