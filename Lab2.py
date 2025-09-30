import pandas as pd
import numpy as np

# 1. Cargar el dataset
df = pd.read_csv("mustafa brand.csv")

# 2. Resumen estadístico
print("Resumen estadístico:")
print(df.describe())

# 3. Tipos de datos
print("Tipos de datos por columna:")
print(df.dtypes)

# 4. Primeros y últimos registros
print("Primeros registros:")
print(df.head())

print("Últimos registros:")
print(df.tail())

# 5. Ordenar por una columna (ajusta el nombre según tu archivo)
# Ejemplo: ordenar por 'Final Grade' si existe
columna_orden = "Final Grade"  # Cambia esto si tu dataset tiene otro nombre
if columna_orden in df.columns:
    print(f"Ordenado por '{columna_orden}':")
    print(df.sort_values(by=columna_orden, ascending=False))
else:
    print(f"\n La columna '{columna_orden}' no existe en el dataset.")

# 6. Medidas estadísticas sobre una columna numérica
columna_estadistica = "Final Grade"  # Cambia esto si tu dataset tiene otro nombre
if columna_estadistica in df.columns and np.issubdtype(df[columna_estadistica].dtype, np.number):
    print(f" Medidas estadísticas para '{columna_estadistica}':")
    print("Media:", np.mean(df[columna_estadistica]))
    print("Mediana:", np.median(df[columna_estadistica]))
    print("Desviación estándar:", np.std(df[columna_estadistica]))
else:
    print(f"La columna '{columna_estadistica}' no es numérica o no existe.")