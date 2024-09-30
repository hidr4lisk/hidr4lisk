import tkinter as tk

# Crear la ventana principal
root = tk.Tk()
root.title("Calculadora de Puntaje de Fútbol")
root.geometry("260x200")  # Ajustar el tamaño para acomodar los elementos

# Etiquetas para cada campo
label_ganados = tk.Label(root, text="Ganados")
label_ganados.grid(row=0, column=0, padx=10, pady=5)

label_empatados = tk.Label(root, text="Empatados")
label_empatados.grid(row=0, column=1, padx=10, pady=5)

label_perdidos = tk.Label(root, text="Perdidos")
label_perdidos.grid(row=0, column=2, padx=10, pady=5)

# Entradas para los datos
entrada_ganados = tk.Entry(root, width=10)
entrada_ganados.grid(row=1, column=0, padx=10, pady=5)

entrada_empatados = tk.Entry(root, width=10)
entrada_empatados.grid(row=1, column=1, padx=10, pady=5)

entrada_perdidos = tk.Entry(root, width=10)
entrada_perdidos.grid(row=1, column=2, padx=10, pady=5)

# Etiqueta para mostrar el resultado
resultado_label = tk.Label(root, text="Puntaje promedio: ")
resultado_label.grid(row=3, column=0, columnspan=3, pady=10)

# Función para calcular el puntaje y mostrarlo en la ventana
def calcular_puntaje():
    try:
        ganados = int(entrada_ganados.get())
        empatados = int(entrada_empatados.get())
        perdidos = int(entrada_perdidos.get())

        # Verificar que la suma de los partidos no supere 20
        if ganados + empatados + perdidos > 20:
            resultado_label.config(text="Error: La suma no puede superar 20 partidos.")
        else:
            puntaje = (ganados * 3 + empatados) / 20
            resultado_label.config(text=f"Puntaje promedio: {puntaje:.2f}")

    except ValueError:
        resultado_label.config(text="Error: Por favor, ingresa solo números válidos.")

# Botón para calcular el puntaje
boton_calcular = tk.Button(root, text="Calcular Puntaje", command=calcular_puntaje)
boton_calcular.grid(row=2, column=0, columnspan=3, pady=10)

# Iniciar el bucle de eventos
root.mainloop()
