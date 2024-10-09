# Importar las bibliotecas necesarias
import gspread  # Para interactuar con Google Sheets
from google.oauth2.service_account import Credentials  # Para la autenticación con Google
import pandas as pd  # Para manejar datos en formato de tabla
import glob  # Para buscar archivos en el sistema
import os  # Para interactuar con el sistema operativo
import tkinter as tk  # Para la interfaz gráfica
from tkinter import messagebox  # Para mostrar mensajes de alerta
from datetime import datetime  # Para obtener la fecha y hora actual

# Definir la ruta del directorio actual (donde está el archivo .py)
current_directory = os.path.dirname(os.path.abspath(__file__))

# Ruta al archivo JSON con las credenciales
json_creds_path = os.path.join(current_directory, 'credenciales_google.json')

# Alcance de la API
scopes = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

# Autenticación
creds = Credentials.from_service_account_file(json_creds_path, scopes=scopes)
client = gspread.authorize(creds)

def seleccionar_hoja_tk():
    # Listado de hojas con nombres descriptivos
    hojas = {
        0: "Emma",
        1: "Pablo",
        2: "Fede"
        # Para agregar más hojas, simplemente añade aquí:
        # 3: "Nombre de la nueva hoja"
    }
    
    # Crear una ventana de Tkinter
    window = tk.Tk()
    window.title("Seleccionar Hoja")
    window.state('zoomed')  # Iniciar la ventana maximizada

    # Crear una etiqueta de título principal
    title_main = tk.Label(window, text="Carga automática Notas recibidas", font=("Arial", 16, "bold"))
    title_main.pack(pady=10)  # Añadir un espacio vertical

    # Crear una etiqueta de título
    title_label = tk.Label(window, text="Selecciona una hoja:", font=("Arial", 12))
    title_label.pack(pady=5)  # Añadir un espacio vertical

    # Variable para guardar la selección
    seleccion = tk.IntVar()

    # Crear etiquetas y botones para cada hoja
    for i, nombre in hojas.items():
        rb = tk.Radiobutton(window, text=f"Hoja {i}: {nombre}", variable=seleccion, value=i, anchor='w')
        rb.pack(pady=5)  # Añadir un espacio vertical entre los botones

    def confirmar_seleccion():
        hoja_seleccionada = seleccion.get()
        if hoja_seleccionada in hojas:
            confirmacion = messagebox.askyesno("Confirmación", f"¿Estás seguro de que deseas seleccionar la hoja de {hojas[hoja_seleccionada]}?")
            if confirmacion:
                window.destroy()  # Cerrar la ventana
                procesar_hoja(hoja_seleccionada)  # Procesar la hoja seleccionada
        else:
            messagebox.showwarning("Advertencia", "Por favor selecciona una hoja.")

    # Botón para confirmar la selección
    btn_confirmar = tk.Button(window, text="Confirmar selección", command=confirmar_seleccion)
    btn_confirmar.pack(pady=10)  # Espacio vertical para el botón

    window.mainloop()  # Iniciar la aplicación

def procesar_hoja(hoja_seleccionada):
    # Abrir el Google Sheet por URL
    sheet = client.open_by_url('https://docs.google.com/spreadsheets/d/1rZQjkpv94q1hmRl0OiGlWpZ325B_newG5H0DmUUv264/edit?usp=sharing')
    
    # Seleccionar la hoja de cálculo específica dentro del Google Sheet
    worksheet = sheet.get_worksheet(hoja_seleccionada)

    # Buscar archivos Excel en el directorio actual
    excel_files = glob.glob(os.path.join(current_directory, "*.xls")) + glob.glob(os.path.join(current_directory, "*.xlsx"))

    if not excel_files:
        messagebox.showinfo("Información", "No se encontró ningún archivo .xls o .xlsx.")
    else:
        latest_file = sorted(excel_files, key=os.path.getmtime)[-1]
        excel_data = pd.read_excel(latest_file)

        for column in ['Fecha Envío', 'Fecha Operación']:
            if column in excel_data.columns:
                excel_data[column] = pd.to_datetime(excel_data[column].str.split(' ').str[0], format='%d-%m-%Y', errors='coerce').dt.strftime('%Y-%m-%d')

        excel_data.fillna('', inplace=True)
        data_to_upload = excel_data.values.tolist()

        existing_data = worksheet.get_all_values()
        new_data = [row for row in data_to_upload if row not in existing_data]

        # Registrar el resultado en el archivo de log
        log_message = f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Hoja: {hoja_seleccionada} - "
        if new_data:
            worksheet.append_rows(new_data)
            log_message += f"Datos nuevos agregados: {len(new_data)}"
            messagebox.showinfo("Éxito", "Datos nuevos agregados al Google Sheet.")
        else:
            log_message += "No hay datos nuevos para agregar."
            messagebox.showinfo("Información", "No hay datos nuevos para agregar.")

        # Guardar el log en un archivo de texto
        log_file_path = os.path.join(current_directory, 'log.txt')
        with open(log_file_path, 'a') as log_file:
            log_file.write(log_message + '\n')

        # Eliminar el archivo Excel después de procesarlo
        os.remove(latest_file)
        messagebox.showinfo("Información", f"Archivo Excel {latest_file} eliminado.")

# Llamar a la función de selección de hoja
seleccionar_hoja_tk()
