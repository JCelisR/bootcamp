import pandas as pd
import numpy as np

# 1. Crear dataset de ejemplo
# Dataset de ejemplo con nulos y duplicados
data = {
    'id': [1, 2, 3, 4, 4, 5, 6, 7, 8, 9],
    'fecha': ['2025-01-01','2025-01-02','2025-01-03','2025-01-04','2025-01-04',
              '2025-01-05','2025-01-06', None, '2025-01-08','2025-01-09'],
    'cliente': ['A','B','C','D','D','E','F','G','H', None],
    'monto': [100.0, 200.5, np.nan, 150.0, 150.0, 300.0, 250.0, 120.0, 80.0, 60.0],
    'categoria': ['retail','corporate','retail','retail','retail','corporate', None, 'retail','retail','corporate'],
    'estado': ['pagado','pendiente','pagado','pagado','pagado','pendiente','pagado','pagado','anulado','pendiente']
}
df = pd.DataFrame(data)

# Guardar dataset de ejemplo para que el usuario pueda ver el CSV original
df.to_csv('C:\\Users\\jceli\\Bootcamp\\Tarea5\\data\\dataset_original_ejemplo.csv', index=False)

# Comenzar el proceso de data wrangling
print("HEAD:")
print(df.head(), "\n")
print("INFO:")
print(df.info(), "\n")
print("DESCRIBE:")
print(df.describe(include='all'), "\n")

# Identificar nulos y duplicados
print("Nulos por columna:")
print(df.isnull().sum(), "\n")
print("Duplicados (filas completas):", df.duplicated().sum(), "\n")
print("Duplicados por id:", df.duplicated(subset=['id']).sum(), "\n")

# 2. Limpieza y transformación de datos

# 2.1 Eliminar duplicados exactos (mantener la primera ocurrencia)
df_clean = df.drop_duplicates()
# 2.2 Si queremos eliminar duplicados por id (mantener la primera)
df_clean = df_clean.drop_duplicates(subset=['id'], keep='first')

# 2.3 Imputación de valores nulos
# - Para 'monto' usaremos la mediana
monto_mediana = df_clean['monto'].median()
df_clean['monto'] = df_clean['monto'].fillna(monto_mediana)

# - Para 'categoria' y 'cliente' usaremos la moda
categoria_moda = df_clean['categoria'].mode(dropna=True)
categoria_fill = categoria_moda[0] if not categoria_moda.empty else 'desconocido'
df_clean['categoria'] = df_clean['categoria'].fillna(categoria_fill)

cliente_moda = df_clean['cliente'].mode(dropna=True)
cliente_fill = cliente_moda[0] if not cliente_moda.empty else 'cliente_desconocido'
df_clean['cliente'] = df_clean['cliente'].fillna(cliente_fill)

# - Para 'fecha' podemos imputar con un valor fijo o eliminar filas.
# Usaré imputar la fecha más frecuente
fecha_moda = df_clean['fecha'].mode(dropna=True)
fecha_fill = fecha_moda[0] if not fecha_moda.empty else '2025-01-01'
df_clean['fecha'] = df_clean['fecha'].fillna(fecha_fill)

# 2.4 Conversión de tipos
df_clean['fecha'] = pd.to_datetime(df_clean['fecha'], errors='coerce')
df_clean['monto'] = df_clean['monto'].astype(float)
df_clean['categoria'] = df_clean['categoria'].astype('category')
df_clean['estado'] = df_clean['estado'].astype('category')

# 2.5 Crear columna nueva: monto en miles (ejemplo de enriquecimiento)
df_clean['monto_miles'] = (df_clean['monto'] / 1000).round(3)

# 2.6 Mapear estados a códigos numéricos
map_estado = {'pagado': 1, 'pendiente': 0, 'anulado': -1}
df_clean['estado_code'] = df_clean['estado'].map(map_estado).fillna(0).astype(int)

# 3. Optimización y estructuración de datos

# 3.1 Reordenar columnas para mejor interpretación
cols_order = ['id','fecha','cliente','categoria','estado','estado_code','monto','monto_miles']
df_clean = df_clean[cols_order]

# 3.2 Filtrado: obtener solo registros con monto mayor a 100
df_filtrado = df_clean[df_clean['monto'] > 100]

# 3.3 Agrupación y agregación: monto total y promedio por categoria
agg_categoria = df_clean.groupby('categoria', observed=False).agg(
    total_monto = ('monto','sum'),
    promedio_monto = ('monto','mean'),
    conteo = ('id','count')
).reset_index()

# 3.4 Ordenar por total_monto descendente
agg_categoria = agg_categoria.sort_values(by='total_monto', ascending=False)

# 4. Exportación de datos
# Guardar DataFrame procesado en CSV y Excel
df_clean.to_csv('C:\\Users\\jceli\\Bootcamp\\Tarea5\\data\\dataset_limpio_ejemplo.csv', index=False)
df_clean.to_excel('C:\\Users\\jceli\\Bootcamp\\Tarea5\\data\\dataset_limpio_ejemplo.xlsx', index=False)

# Guardar agregaciones
agg_categoria.to_csv('C:\\Users\\jceli\\Bootcamp\\Tarea5\\data\\agg_categoria_ejemplo.csv', index=False)

# Resultados finales 
print("DATAFRAME LIMPIO - HEAD:")
print(df_clean.head(), "\n")
print("AGREGACION POR CATEGORIA:")
print(agg_categoria, "\n")
print("DATAFRAME FILTRADO (monto > 100) - HEAD:")
print(df_filtrado.head(), "\n")