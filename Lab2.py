import pandas as pd
import numpy as np

# 1. Cargar el dataset
df = pd.read_csv("mustafa brand.csv")

# 2. Resumen estadístico
print("--Resumen estadístico:")
print(df.describe())

# 3. Tipos de datos
print("--Tipos de datos por columna:")
print(df.dtypes)

# 4. Primeros y últimos registros
print("--Primeros registros:")
print(df.head())

print("--Últimos registros:")
print(df.tail())

# 5. Ordenar por calificaciones obtenidas
print("--Ordenado por 'obtain m':")
print(df.sort_values(by="obtain m", ascending=False))

# 6. Medidas estadísticas sobre 'obtain m'
columna_estadistica = "obtain m"
if columna_estadistica in df.columns and np.issubdtype(df[columna_estadistica].dtype, np.number):
    print(f"--Medidas estadísticas para '{columna_estadistica}':")
    print("Media:", np.mean(df[columna_estadistica]))
    print("Mediana:", np.median(df[columna_estadistica]))
    print("Desviación estándar:", np.std(df[columna_estadistica]))
else:
    print(f"--La columna '{columna_estadistica}' no es numérica o no existe.")