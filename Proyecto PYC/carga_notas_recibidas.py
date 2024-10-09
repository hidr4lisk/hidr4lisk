# Importar las bibliotecas necesarias
# pip install gspread pandas oauth2client openpyxl
# compilar
# pyinstaller --onefile --name "Carga Automatica" --add-data "credenciales_google.json;." cargar_notas_recibidas.py

import gspread
from google.oauth2.service_account import Credentials
import pandas as pd
import os
import sys
from datetime import datetime

# Obtener el directorio del ejecutable o script
if getattr(sys, 'frozen', False):
    # Si está ejecutado como un ejecutable PyInstaller
    current_directory = sys._MEIPASS
else:
    # Si está ejecutado como un script
    current_directory = os.path.dirname(os.path.abspath(__file__))

# Ruta al archivo JSON con las credenciales de Google
json_creds_path = os.path.join(current_directory, 'credenciales_google.json')

# Alcance de la API
scopes = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

# Autenticación con Google API
creds = Credentials.from_service_account_file(json_creds_path, scopes=scopes)
client = gspread.authorize(creds)

# Función principal
def main():
    while True:
        print("Seleccione hoja a actualizar:")
        print("""
        ┌─────┬─────────┐
        │ Nº  │ Nombre  │
        ├─────┼─────────┤
        │ 0   │ Emma    │
        │ 1   │ Pablo   │
        │ 2   │ Fede    │
        │ 3   │ Mariano │
        │ 4   │ Pipo    │
        │ 5   │ Euge    │
        └─────┴─────────┘
        """)

        try:
            hoja_seleccionada = int(input("Elige una opción (0-5): "))
            if hoja_seleccionada < 0 or hoja_seleccionada > 5:
                raise ValueError
            break  # Salir del bucle si la entrada es válida
        except ValueError:
            print("Opción inválida. Por favor, ingresa un número entre 0 y 5.")

    # Buscar automáticamente el primer archivo Excel en el directorio actual
    file_path = None
    for file in os.listdir(current_directory):
        if file.endswith('.xls') or file.endswith('.xlsx'):
            file_path = os.path.join(current_directory, file)
            break

    if file_path is None:
        print(f"No se encontró ningún archivo Excel en el directorio {current_directory}.")
        return

    procesar_excel(file_path, hoja_seleccionada)

# Función para procesar el archivo Excel seleccionado
def procesar_excel(file_path, hoja_seleccionada):
    sheet = client.open_by_url('https://docs.google.com/spreadsheets/d/1rZQjkpv94q1hmRl0OiGlWpZ325B_newG5H0DmUUv264/edit?usp=sharing')
    worksheet = sheet.get_worksheet(hoja_seleccionada)
    excel_data = pd.read_excel(file_path)

    for column in ['Fecha Envío', 'Fecha Operación']:
        if column in excel_data.columns:
            excel_data[column] = pd.to_datetime(excel_data[column].str.split(' ').str[0], format='%d-%m-%Y', errors='coerce').dt.strftime('%Y-%m-%d')

    excel_data.fillna('', inplace=True)
    data_to_upload = excel_data.values.tolist()

    existing_data = worksheet.get_all_values()
    new_data = [row for row in data_to_upload if row not in existing_data]

    log_message = f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Hoja: {hoja_seleccionada} - "

    if new_data:
        worksheet.append_rows(new_data)
        log_message += f"Datos nuevos agregados: {len(new_data)}"
        print("Datos nuevos agregados al Google Sheet.")
    else:
        log_message += "No hay datos nuevos para agregar."
        print("No hay datos nuevos para agregar.")

    log_file_path = os.path.join(current_directory, 'log.txt')
    with open(log_file_path, 'a') as log_file:
        log_file.write(log_message + '\n')

if __name__ == "__main__":
    main()
