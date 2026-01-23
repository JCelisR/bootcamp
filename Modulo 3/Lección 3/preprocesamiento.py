import pandas as pd
import numpy as np

# 1. Carga
na_vals = ['?', 'N/A', 'NaN', '']
tipos = {'ID': 'int32', 'Nombre': 'string', 'Edad': 'float32', 'Ciudad': 'string', 'Salario': 'float32', 'Estado': 'category'}
df = pd.read_csv('C:\\Users\\jceli\\Bootcamp\\Modulo 3\\Lección 3\\datos_ejemplo.csv', na_values=na_vals, dtype=tipos, parse_dates=['Fecha'], dayfirst=False)

# COMIENZO
print("Resumen inicial:")
print(df.info())
print(df.isnull().sum())

df = df.drop_duplicates()		# Eliminar duplicados exactos
df = df.dropna(subset=['Nombre'])	# Manejo de valores críticos faltantes, si falta Nombre (clave), eliminamos; Edad y Salario se imputan.

edad_mediana = df['Edad'].median()				# 2c. Imputación
df['Edad'] = df['Edad'].fillna(edad_mediana).astype('int8')	# Edad: usar mediana (robusta frente a outliers)

df['Salario'] = df.groupby('Ciudad')['Salario'].transform(lambda x: x.fillna(x.mean()))	# Salario: imputar con media por ciudad si posible, sino con media global
df['Salario'] = df['Salario'].fillna(df['Salario'].mean()).astype('float32')

df['Fecha'] = pd.to_datetime(df['Fecha'], errors='coerce')	# Fecha: convertir errores a NaT y eliminar si es crítico
df = df.dropna(subset=['Fecha'])

df['Estado'] = df['Estado'].astype('category')

cols_relevantes = ['ID','Nombre','Edad','Ciudad','Salario','Fecha','Estado']		# 3. Transformación
df = df[cols_relevantes]
df = df.rename(columns={'Nombre':'nombre','Edad':'edad','Ciudad':'ciudad','Salario':'salario','Fecha':'fecha','Estado':'estado'})

df = df.sort_values(by='fecha', ascending=False)			# Ordenar por fecha descendente

df.to_csv('datos_ejemplo_limpio.csv', index=False)			# 4. Exportación

print("Limpieza completada. Guardado como datos_ejemplo_limpio.csv")
print(df.head())
