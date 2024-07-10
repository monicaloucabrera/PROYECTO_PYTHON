import requests #importamos el modulo requests para las peticiones HTTP
from bs4 import BeautifulSoup #importamos beatiful spou para analizar un documento HTML
import pandas as pd #importamos pandas para manejar los datos

def fetch_page(url):
    #Obtenemos el contenido de una pagina
    
    response= requests.get(url)#Realizamos una solicitud GET a la url
    print("entra a fetch_page") 

    #print(response)
    
    
    if response.status_code==200:
        return response.content #devolvemos el contenido de la pagina si la solicitud fue exitosa
    else:
        raise Exception(f"Failed to fetch page: {url}")#lanzamos una excepton si la solicitud falla
    

    
#print (fetch_page(base_url))
def parse_product(product):
    #Nalizamos los detalles de un producto
    title = product.find("div", class_="s-item__title" ).text.strip()
    price = product.find("span",class_="s-item__price").text.strip()
    
    return{#retornamos el dicionario
            "title":title,
            #"description":description,
            "price":price,
        }



###def parse_product(product): FUNCION ORIGINAL
    #Nalizamos los detalles de un producto
 #   title= product.find ("a", class_="title").text.strip()#Encontramos y obtenemos el titulo del producto
 #   description = product.find ("p", class_="description").text.strip()#obtenemos la desc ripcion del producto
 #   price = product.find("h4",class_="price").text.strip()
 #   return{#retornamos el dicionario
 #       "title":title,
 #       "description":description,
 #       "price":price,
 #   }
    
def scrape(url):
    #Funcion principal del scraping
    page_content = fetch_page(url)#Obtenemos el codigo HTML dela pagina
    soup = BeautifulSoup(page_content,"html.parser")#Analizamos el contenido con Beatifullsoup
    #print(soup.prettify())  
    #products = soup.find_all("div",class_="thumbnail")#Enconntramos todos los elementos div con la clase thumbail de los productos
    #products = soup.find_all ("div", class_ ="s-item__title")
    products = soup.find_all("li", class_="s-item s-item__pl-on-bottom")
    #print (products)
    #Guardamos los productos en un arreglo
    products_data=[]#inicializamos una lista para almacenar los datos de losproductos
    
    for product in products:
        product_info = parse_product(product) #analizamos cada producto
        products_data.append(product_info) #agragams el producto a la lista"""
    
    #print(products_data)
    
    return pd.DataFrame(products_data)

    
#    print(products)
#definmo la url base    
##base_url = "https://webscraper.io/test-sites/e-commerce/allinone"


base_url = "https://www.ebay.com/sch/i.html?_from=R40&_trksid=p4432023.m570.l1311&_nkw=iphone+14+pro+max&_sacat=0"

#print(scrape(base_url))
#llamamos a la funcion scrape con la url
df = scrape(base_url)
print(df)
#Guardamos los datos en un archivo csv

df.to_csv("data/raw/products.csv",index=False)

    
 
