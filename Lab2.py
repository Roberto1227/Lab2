import pandas as pd
import numpy as np

def cargar_dataset(ruta):
    """
    Carga el dataset desde un archivo CSV.
    """
    try:
        df = pd.read_csv(ruta)
        print(f"✅ Dataset cargado correctamente desde '{ruta}'.\n")
        return df
    except FileNotFoundError:
        print(f"❌ Error: El archivo '{ruta}' no se encontró.")
        return None
    except Exception as e:
        print(f"❌ Error al cargar el archivo: {e}")
        return None

def mostrar_resumen(df):
    """
    Muestra un resumen estadístico general del dataset.
    """
    print("📊 Resumen estadístico general (describe()):")
    print(df.describe(include='all'))
    print("\n")

def mostrar_tipos_datos(df):
    """
    Muestra los tipos de datos de cada columna y sugiere posibles análisis.
    """
    print("🔎 Tipos de datos por columna (dtypes):")
    print(df.dtypes)
    print("\nSugerencia de análisis:")
    for col, tipo in df.dtypes.items():
        if np.issubdtype(tipo, np.number):
            print(f"- '{col}': Numérica ➡️ Se pueden calcular media, mediana, desviación estándar, etc.")
        else:
            print(f"- '{col}': No numérica ➡️ Se pueden analizar frecuencias, valores únicos, etc.")
    print("\n")

def mostrar_head_tail(df):
    """
    Muestra los primeros y últimos registros del dataset.
    """
    print("🔝 Primeros 5 registros (head()):")
    print(df.head())
    print("\n🔚 Últimos 5 registros (tail()):")
    print(df.tail())
    print("\n")

def ordenar_por_columna(df):
    """
    Permite al usuario ordenar el dataset por una columna específica.
    """
    print("📋 Columnas disponibles para ordenar:", list(df.columns))
    columna = input("¿Por qué columna deseas ordenar? (deja vacío para omitir): ").strip()
    if columna and columna in df.columns:
        print(f"\n🔽 Top 10 registros ordenados por '{columna}':")
        print(df.sort_values(by=columna, ascending=False).head(10))
    elif columna:
        print(f"❌ La columna '{columna}' no existe en el dataset.")
    print("\n")

def estadisticas_columna(df):
    """
    Permite al usuario calcular media, mediana y desviación estándar de una columna numérica.
    """
    columnas_numericas = list(df.select_dtypes(include=np.number).columns)
    print("🔢 Columnas numéricas disponibles:", columnas_numericas)
    columna = input("¿Sobre qué columna numérica deseas calcular estadísticas? (deja vacío para omitir): ").strip()
    if columna and columna in columnas_numericas:
        print(f"\n📈 Medidas estadísticas para '{columna}':")
        print("Media:", np.mean(df[columna]))
        print("Mediana:", np.median(df[columna]))
        print("Desviación estándar:", np.std(df[columna]))
    elif columna:
        print(f"❌ La columna '{columna}' no es numérica o no existe.")
    print("\n")

def main():
    ruta = "mustafa brand.csv"  # Cambia el nombre si tu archivo es diferente
    df = cargar_dataset(ruta)
    if df is not None:
        mostrar_resumen(df)         # Punto 2
        mostrar_tipos_datos(df)     # Punto 3
        mostrar_head_tail(df)       # Punto 4
        ordenar_por_columna(df)     # Punto 5
        estadisticas_columna(df)    # Punto 6

if __name__ == "__main__":
    main()