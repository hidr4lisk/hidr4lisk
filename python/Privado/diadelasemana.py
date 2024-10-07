import time
import tkinter as tk
from tkinter import messagebox

def obtener_dia_semana(dia, mes, año):
    # Crear una fecha en formato YYYY-MM-DD
    fecha_str = f"{año}-{mes}-{dia}"
    try:
        # Analizar la fecha ingresada
        fecha_t = time.strptime(fecha_str, "%Y-%m-%d")
        # Obtener el día de la semana (0 = lunes, 1 = martes, ..., 6 = domingo)
        dia_semana_numero = fecha_t.tm_wday
        # Lista de nombres de días
        dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
        # Obtener el nombre del día
        return dias[dia_semana_numero]
    except ValueError:
        return None

def verificar_fecha():
    dia = entrada_dia.get()
    mes = entrada_mes.get()
    año = entrada_año.get()
    
    if dia.isdigit() and mes.isdigit() and año.isdigit():
        dia = int(dia)
        mes = int(mes)
        año = int(año)
        
        dia_semana = obtener_dia_semana(dia, mes, año)
        if dia_semana:
            resultado.config(text=f"La fecha {dia}/{mes}/{año} corresponde a un {dia_semana}.")
        else:
            resultado.config(text="Fecha inválida. Por favor, intenta de nuevo.")
    else:
        messagebox.showerror("Error", "Por favor, ingresa números válidos.")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Verificar Día de la Semana")
ventana.geometry("400x200")
ventana.configure(bg="white")

# Crear un Frame para los cuadros de entrada
frame_entrada = tk.Frame(ventana, bg="white")
frame_entrada.pack(pady=10)

# Etiquetas y entradas para el día, mes y año en una línea
etiqueta_dia = tk.Label(frame_entrada, text="Día:", font=("Arial", 14), fg="black", bg="white")
etiqueta_dia.pack(side=tk.LEFT, padx=5)
entrada_dia = tk.Entry(frame_entrada, width=5, font=("Arial", 14))
entrada_dia.pack(side=tk.LEFT, padx=5)

etiqueta_mes = tk.Label(frame_entrada, text="Mes:", font=("Arial", 14), fg="black", bg="white")
etiqueta_mes.pack(side=tk.LEFT, padx=5)
entrada_mes = tk.Entry(frame_entrada, width=5, font=("Arial", 14))
entrada_mes.pack(side=tk.LEFT, padx=5)

etiqueta_año = tk.Label(frame_entrada, text="Año:", font=("Arial", 14), fg="black", bg="white")
etiqueta_año.pack(side=tk.LEFT, padx=5)
entrada_año = tk.Entry(frame_entrada, width=5, font=("Arial", 14))
entrada_año.pack(side=tk.LEFT, padx=5)

# Botón para verificar la fecha
boton = tk.Button(ventana, text="Verificar", command=verificar_fecha, font=("Arial", 14), fg="black", bg="lightgray")
boton.pack(pady=20)

# Etiqueta para mostrar el resultado
resultado = tk.Label(ventana, text="", font=("Arial", 14), fg="black", bg="white")
resultado.pack(pady=10)

# Ejecutar la aplicación
ventana.mainloop()
