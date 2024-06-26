import pandas as pd

# Nombre del archivo CSV
file_path = 'unified_experts.csv'

# Cargar el archivo CSV
df = pd.read_csv(file_path, delimiter=';', low_memory=False)

# Eliminar registros sin email
df = df.dropna(subset=['Email'])

# Convertir todos los correos electrónicos a minúsculas y asegurarse de que sean cadenas
df['Email'] = df['Email'].astype(str).str.lower()

# Verificar duplicados en la columna "Email"
duplicate_emails = df[df.duplicated(subset=['Email'], keep=False)]['Email']

# Contar duplicados por email
email_counts = duplicate_emails.value_counts()

# Crear un DataFrame con los resultados
report_df = pd.DataFrame({
    'Email': email_counts.index,
    'Cantidad de Duplicados': email_counts.values
})

# Calcular el total de registros duplicados a eliminar
total_duplicados = len(duplicate_emails)

# Añadir el total de registros duplicados al DataFrame
total_row = pd.DataFrame({
    'Email': ['Total de registros duplicados a eliminar'],
    'Cantidad de Duplicados': [total_duplicados]
})
report_df = pd.concat([report_df, total_row], ignore_index=True)

# Escribir el reporte en un archivo Excel
report_file_path = 'email_duplicates_report2.xlsx'
with pd.ExcelWriter(report_file_path) as writer:
    report_df.to_excel(writer, sheet_name='Reporte de Duplicados', index=False)

# Formatear correos duplicados en grupos de 20
duplicate_emails_list = duplicate_emails.unique().tolist()
groups_of_20 = [duplicate_emails_list[i:i + 20] for i in range(0, len(duplicate_emails_list), 20)]

# Generar el contenido del archivo de texto
formatted_groups = []
for group in groups_of_20:
    formatted_group = "','".join(group)
    formatted_groups.append(f"('{formatted_group}')")

# Escribir los grupos formateados en un archivo de texto
text_file_path = 'duplicated_emails_formatted.txt'
with open(text_file_path, 'w') as file:
    file.write('\n\n'.join(formatted_groups))

print(f"Archivo '{report_file_path}' generado con éxito.")
print(f"Archivo '{text_file_path}' generado con éxito.")
