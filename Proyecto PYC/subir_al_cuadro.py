import gspread
from google.oauth2.service_account import Credentials
import pandas as pd
import glob
import os

# Ruta al archivo JSON con las credenciales
json_creds_path = r'C:\Users\Sinli\OneDrive\Documentos\py practice\Proyecto PYC\credenciales_google.json'

# Alcance de la API
scopes = ['https://www.googleapis.com/auth/spreadsheets',
          'https://www.googleapis.com/auth/drive']

# Autenticación
creds = Credentials.from_service_account_file(json_creds_path, scopes=scopes)
client = gspread.authorize(creds)

# Abrir el Google Sheet por URL
sheet = client.open_by_url('https://docs.google.com/spreadsheets/d/1rZQjkpv94q1hmRl0OiGlWpZ325B_newG5H0DmUUv264/edit?usp=sharing')
worksheet = sheet.get_worksheet(2)  # 0=Emma 1=Pablo 2=Yo

# Definir la ruta del directorio actual
current_directory = r'C:\Users\Sinli\OneDrive\Documentos\py practice\Proyecto PYC'

# Buscar archivos Excel en el directorio actual
excel_files = glob.glob(os.path.join(current_directory, "*.xls")) + glob.glob(os.path.join(current_directory, "*.xlsx"))
if not excel_files:
    print("No se encontró ningún archivo .xls o .xlsx.")
else:
    # Cargar el último archivo Excel encontrado
    latest_file = sorted(excel_files, key=os.path.getmtime)[-1]  # El último archivo modificado
    excel_data = pd.read_excel(latest_file)

    # Convertir las columnas 'Fecha Envío' y 'Fecha Operación' al formato deseado
    for column in ['Fecha Envío', 'Fecha Operación']:
        if column in excel_data.columns:
            # Convertir las fechas en formato "DD-MM-YYYY hora" a "YYYY-MM-DD"
            excel_data[column] = pd.to_datetime(excel_data[column].str.split(' ').str[0], format='%d-%m-%Y', errors='coerce').dt.strftime('%Y-%m-%d')

    # Reemplazar valores NaN por una cadena vacía
    excel_data.fillna('', inplace=True)

    # Convertir DataFrame a lista de listas para cargar en Google Sheets
    data_to_upload = excel_data.values.tolist()

    # Obtener las filas actuales del Google Sheet para verificar duplicados
    existing_data = worksheet.get_all_values()

    # Filtrar solo las filas que no estén ya en el Google Sheet
    new_data = [row for row in data_to_upload if row not in existing_data]

    # Si hay datos nuevos, subirlos
    if new_data:
        worksheet.append_rows(new_data)
        print("Datos nuevos agregados al Google Sheet.")
    else:
        print("No hay datos nuevos para agregar.")
