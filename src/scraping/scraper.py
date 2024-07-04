import requests # Importar el modulo requests para hacer las solicitudes HTTP

from bs4 import BeautifulSoup # Importar BeautifulSoup para analizar el contenido HTML

import pandas as pd # Importar el modulo pandas para crear un DataFrame

def fetch_page(url):
    # Realizar una solicitud HTTP GET a la URL proporcionada para obtener el contenido de la página
    response = requests.get(url)
    if response.status_code == 200: #Significa petición exitosa
        return response.content #Devuelve el contenido de la página
    else:
        raise Exception(f"Failed to fetch page: {url}") #Excepcion para petición fallida
    

def parse_product(html_content):
    # Analizar el contenido HTML y extraer información relevante    
    title = html_content.find("a", class_= "title").text.strip() #Extraer el texto del título
    description = html_content.find("p", class_=  "description").text.strip() #Extraer el texto de la descripción
    price = html_content.find("h4", class_= "price").text.strip() #Extraer el texto del precio
    return { #Devolver un diccionario
        "title": title,
        "description": description,
        "price": price
    }
    
def scrape(url):
    # Función para extraer información de una página web. Funcion principal del scraping
    page_content = fetch_page(url) # Obtener el contenido de la página
    soup = BeautifulSoup(page_content, "html.parser") # Analizar el contenido HTML
    products = soup.find_all("div", class_=  "thumbnail") # Buscar todos los elementos div con la clase "thumbnail"
    
    products_data = [] #Incializamos una lista para almacenar los datos de los productos
    
    for product in products:
        product_info = parse_product(product)
        products_data.append(product_info) #Añadir los datos de cada producto a la lista
    print(products_data)
    return pd.DataFrame(products_data) #Devolver un diccionario 
    
url = "https://webscraper.io/test-sites/e-commerce/allinone"

df = scrape(url)

print(df)

df.to_csv("data/raw/products.csv", index = False) #Guardamos los datos en un archivo csv sin incluir indice
