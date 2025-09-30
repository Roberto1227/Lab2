import pandas as pd
import numpy as np

# 1. Cargar el dataset
df = pd.read_csv("mustafa brand.csv")

print("="*50)
print("ANÁLISIS DEL DATASET: Student Result")
print("="*50)

# 2. Resumen estadístico
print("\n[1] Resumen estadístico de columnas numéricas:")
print(df.describe().round(2))

# 3. Tipos de datos
print("\n[2] Tipos de datos por columna:")
print(df.dtypes)

# 4. Primeros y últimos registros
print("\n[3] Primeros 5 registros:")
print(df.head())

print("\n[4] Últimos 5 registros:")
print(df.tail())

# 5. Ordenar por calificaciones obtenidas
print("\n[5] Top 5 estudiantes con mayor calificación ('obtain m'):")
print(df.sort_values(by="obtain m", ascending=False).head())

print("\n[6] Top 5 estudiantes con menor calificación ('obtain m'):")
print(df.sort_values(by="obtain m", ascending=True).head())

# 6. Medidas estadísticas sobre 'obtain m'
columna_estadistica = "obtain m"
if columna_estadistica in df.columns and np.issubdtype(df[columna_estadistica].dtype, np.number):
    media = np.mean(df[columna_estadistica])
    mediana = np.median(df[columna_estadistica])
    desviacion = np.std(df[columna_estadistica])
    print(f"\n[7] Medidas estadísticas para '{columna_estadistica}':")
    print(f"   - Media: {media:.2f}")
    print(f"   - Mediana: {mediana:.2f}")
    print(f"   - Desviación estándar: {desviacion:.2f}")
else:
    print(f"\n[7] La columna '{columna_estadistica}' no es numérica o no existe.")

print("\n" + "="*50)
print("Fin del análisis")
print("="*50)