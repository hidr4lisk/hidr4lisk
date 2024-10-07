let zoomed = false;

setInterval(function() {
    if (zoomed) {
        document.body.style.backgroundSize = "cover"; // Tamaño original
    } else {
        document.body.style.backgroundSize = "200%"; // Duplicar tamaño
    }
    zoomed = !zoomed; // Alterna el estado
}, 1000); // Cambia cada 1000 ms (1 segundo)
