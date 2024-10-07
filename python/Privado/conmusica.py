import yt_dlp
import vlc
import time
import tkinter as tk


# Función para verificar si el año es bisiesto
def año_bisiesto(x):
    if (x % 4 == 0 and x % 100 != 0) or (x % 400 == 0):
        return True
    else:
        return False

# Función que se ejecuta al hacer clic en el botón
def verificar_bisiesto():
    entrada = entrada_año.get()
    if entrada.isdigit():  # Verifica si es un número
        año = int(entrada)
        if año_bisiesto(año):
            resultado = f"El año {año} es bisiesto."
        else:
            resultado = f"El año {año} no es bisiesto."
    else:
        resultado = "Por favor, ingresa un número válido."
    
    # Actualizar el texto del label con el resultado
    label_resultado.config(text=resultado)

# Obtener el enlace de audio desde YouTube con yt-dlp
def obtener_enlace_audio(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'quiet': True,
        'no_warnings': True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=False)
        audio_url = info_dict['url']
    return audio_url

# URL del video de YouTube
url = "https://youtu.be/mvlYZW3SCXg?si=ytY1oIMSMpd0d09t"  # Reemplaza con el enlace de tu video

# Obtener el enlace de audio
audio_url = obtener_enlace_audio(url)

# Iniciar el reproductor VLC
player = vlc.MediaPlayer(audio_url)
player.play()

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Verificar Año Bisiesto")
ventana.geometry("400x250")
ventana.configure(bg="white")

# Etiqueta y entrada para ingresar el año
etiqueta = tk.Label(ventana, text="Ingresa un año:", font=("Arial", 14), fg="black", bg="white")
etiqueta.pack(pady=10)

entrada_año = tk.Entry(ventana, font=("Arial", 14))
entrada_año.pack(pady=10)

# Botón para verificar si es bisiesto
boton = tk.Button(ventana, text="Verificar", command=verificar_bisiesto, font=("Arial", 14), fg="black", bg="lightgray")
boton.pack(pady=20)

# Casillero donde se mostrará el resultado
label_resultado = tk.Label(ventana, text="", font=("Arial", 14), fg="black", bg="white")
label_resultado.pack(pady=10)

# Ejecutar la aplicación
ventana.mainloop()

# Parar el audio cuando se cierre la ventana
player.stop()
