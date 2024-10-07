import tkinter as tk

# Crear la ventana principal
root = tk.Tk()
root.title("Ejemplo de Entry con Tkinter")
root.geometry("300x200")

# Crear una etiqueta para mostrar el texto
label = tk.Label(root, text="Introduce tu nombre:")
label.pack(pady=10)

# Crear un cuadro de texto (Entry) para la entrada del usuario
entrada = tk.Entry(root, width=30)
entrada.pack(pady=5)

# Función que se ejecuta cuando se hace clic en el botón
def mostrar_texto():
    nombre = entrada.get()  # Obtener el texto del Entry
    label.config(text=f"¡Hola, {nombre}!")  # Mostrar el texto en la etiqueta

# Crear un botón que ejecutará la función cuando se haga clic
boton = tk.Button(root, text="Mostrar Nombre", command=mostrar_texto)
boton.pack(pady=10)

# Iniciar el bucle de eventos
root.mainloop()
