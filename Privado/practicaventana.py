import tkinter as tk

# Función que será llamada cuando se presione el botón
def obtener_texto():
    texto_ingresado = entry.get()  # Obtenemos el texto del cuadro de texto
    resultado.config(text=f"Has ingresado: {texto_ingresado}")  # Mostramos el resultado debajo
    # Aquí puedes hacer lo que necesites con el texto ingresado
    # Ejemplo: print(texto_ingresado)

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Ingresar texto")
ventana.geometry("300x200")

# Etiqueta para instruir al usuario
label = tk.Label(ventana, text="Ingrese un texto:")
label.pack(pady=10)

# Cuadro de texto para ingresar
entry = tk.Entry(ventana, width=30)
entry.pack(pady=5)

# Botón para obtener el texto ingresado
boton = tk.Button(ventana, text="Mostrar", command=obtener_texto)
boton.pack(pady=10)

# Etiqueta para mostrar el resultado debajo
resultado = tk.Label(ventana, text="")
resultado.pack(pady=10)

# Ejecutamos el loop principal de la ventana
ventana.mainloop()
