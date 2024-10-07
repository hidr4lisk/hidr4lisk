import tkinter as tk
from tkinter import messagebox

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
        messagebox.showinfo("Resultado", resultado)
    else:
        messagebox.showerror("Error", "Por favor, ingresa un número válido.")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Verificar Año Bisiesto")
ventana.geometry("400x200")
ventana.configure(bg="white")

# Etiqueta y entrada para ingresar el año
etiqueta = tk.Label(ventana, text="Ingresa un año:", font=("Arial", 14), fg="black", bg="white")
etiqueta.pack(pady=10)

entrada_año = tk.Entry(ventana, font=("Arial", 14))
entrada_año.pack(pady=10)

# Botón para verificar si es bisiesto
boton = tk.Button(ventana, text="Verificar", command=verificar_bisiesto, font=("Arial", 14), fg="black", bg="lightgray")
boton.pack(pady=20)

# Ejecutar la aplicación
ventana.mainloop()
