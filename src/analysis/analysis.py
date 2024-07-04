import pandas as pd # Importar el modulo pandas para crear un DataFrame. Para manejar y analizar datos
import os # Importar el modulo os para interactuar con el sistema operativo
from ..decorators.decorators import * # Importar el modulo de decoradores


@logit
@timeit
def load_data(data_path):
    """Cargar los datos de un archivo CSV o excel"""
    
    if data_path.endswith(".csv"):
        df = pd.read_csv(data_path) # Carga de datos de un archivo CSV
    elif data_path.endswith(".xlsx"):
        df = pd.read_excel(data_path) # Carga de datos de un archivo Excel
    else:
        raise ValueError("El archivo debe ser un archivo CSV o Excel")
    print ("Carga de datos exitosa")
    return df #Devuelve un DataFrame con los datos cargados

print(load_data("data/raw/products.csv"))

@logit
@timeit
def clean_data(df):
    """Limpia los datos de un DataFrame"""
    df["price"] = df["price"].replace(r"[\$,]", "", regex=True ).astype(float) # Limpiamos y convertimos la columna de precios a tipo float
    
    ## Antes era $1,299.99
    ## Ahora es 1299.99
    
    print ("Limpieza de datos exitosa")
    return df #Devuelve un DataFrame con los datos formateados

@logit
@timeit
def analyze_data(df):
    """Analiza los datos de un DataFrame"""
    print ("Basic Data Analysis:") #Imprimimos un encabezado para el analisis de datos
    print (df.describe()) #Imprimimos un resumen estadistico de los datos
    print ("\nProducts with highest prices:") #Imprimimos un encabezado para los productos con los precios mas altos 
    # print(df.nlargest(5, "price")) #Imprimimos los 5 productos con los precios mas altos
    hihghestPrices = df.nlargest(5, "price") #Guardamos los 5 productos con los precios mas altos en una variable
    print(hihghestPrices) #Imprimimos los 5 productos con los precios mas altos
    
@logit
@timeit
def save_clean_data(df, output_path):
    """Guarda los datos limpios en un archivo CSV o Excel"""
    if output_path.endswith(".csv"):
        df.to_csv(output_path, index=False) #Guarda los datos en un archivo CSV
    elif output_path.endswith(".xlsx"):
        df.to_excel(output_path, index=False) #Guarda los datos en un archivo Excel
    else:
        raise ValueError("El archivo debe ser un archivo CSV o Excel")
    print (f"Clean data saved to {output_path}")

if __name__ == "__main__": #Permitimos que el script solo se ejecute en este archivo 
    data_path = "data/raw/products.csv" #Ruta del archivo de datos SIN procesar
    output_path = "data/procesado/cleaned_products.csv" #Definimos la ruta del archivo de datos PROCESADO
    
    df = load_data(data_path)
    df = clean_data(df)
    analyze_data(df)
    os.makedirs("data/procesado", exist_ok=True) #Creamos el directorio para los datos procesados si no existe
    save_clean_data(df, output_path)