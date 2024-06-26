import pandas as pd
import csv

# Función para leer y limpiar un CSV
def read_and_clean_csv(file_path):
    try:
        # Leer el archivo CSV
        df = pd.read_csv(file_path, delimiter=',', on_bad_lines='skip', quoting=csv.QUOTE_NONE, encoding='utf-8')
        # Eliminar filas completamente vacías
        df.dropna(how='all', inplace=True)
        return df
    except Exception as e:
        print(f"Error al leer {file_path}: {e}")
        return pd.DataFrame()

# Lista de archivos CSV a unificar
csv_files = ['Experts recruit_C_001-2.csv', 'Experts recruit_C_002-2.csv', 'Experts recruit_C_003-2.csv']

# Leer y limpiar cada archivo CSV
dataframes = [read_and_clean_csv(file) for file in csv_files]

# Concatenar todos los DataFrames en uno solo
combined_df = pd.concat(dataframes, ignore_index=True)

# Guardar el DataFrame combinado en un nuevo archivo CSV
combined_df.to_csv('unified_output.csv', index=False)

print("Archivos CSV unificados correctamente en 'unified_output.csv'")