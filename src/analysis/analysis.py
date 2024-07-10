import pandas as pd #importamos panda para el analisis d datos
import os #importamos os para interactuar con el sistema operativo
#import decorators


#from  ..decorators.decorators import timeit, logit #importamos los decoradores personalizados

#import C:\PROYECTO_PYTHON\src\decorators\decorators.py
#print(sys.path)

#@logit #Añadimos el loggin a la funcion
#@timeit #Medimos el tiempo de ejecudciòn de uan funcion
def load_data(data_path): 
    #carga los datos desde un archivo csv o excel, en nuestro caso el archivo products.csv
    
    if data_path.endswith(".csv"):
        df = pd.read_csv(data_path)  #cargamos el archivo en formato csv
    elif data_path.endswitch(".xlsx"): #cargamos el archivo en excel
        df = pd.read_excel(data_path)
    else:
        raise ValueError("Unsopported file format") #enviamos un mensaje si no es de del formato csv o excel
    print("Data loaded succesfully") #Imprimimos un mensaje indicando que los datos fueron cargados exitosamente
    
    return df #devolvemos el dataframe con los datos cargados

#print(load_data("data/raw/products.csv"))

#creamos una funcion que limpie los datos
#@logit #Añadimos el loggin a la funcion
#@timeit #Medimos el tiempo de ejecudciòn de uan funcion
def clean_data(df):
    print("Ingresa funcion clean_data")
    #df["price"] = df["price"].replace(r"[\$,]","",regex=True).astype(float)#limpiamos y convertimos la columna de precios a tipo float
    #df["price"] = df["price"].replace(r"[\USD,]","",regex=True).astype(float)
    df["price"] = df["price"].replace ({'$':" ",'U':" ",'S':" ",'D':" "},regex=True)
    print(df.dtypes)
    print(df["price"])
    df["price"] = pd.to_numeric (df["price"] , errors='coerce')
    #Antes era USD560.00 de tipo object ahora es 560.0 numerico
    print("Data cleaned Successfully")
    return df #retornamos el dataframe



#@logit #Añadimos el loggin a la funcion
#@timeit #Medimos el tiempo de ejecudciòn de uan funcion
def analyze_data(df):
    ##Realizamos un aanlisis basico de datos
    print("Basic data Analysis:") #Imprimimos un encabezado para el analisis
    print(df.describe())#Imprimimos un resumen estadistico de los datos
    print("\nProducts with highest prices: ")#Imprimimos un encabezado para los productos con los precios mas altos
    highestPrices= df.nlargest(5,'price')
    print(highestPrices) #Imprimimos los 5 productos ocn los precios mas altos
    ##Listamos los productos con los mas bajos precios
    print("\nProducts with lowest prices: ")#Imprimimos un encabezado para los productos con los precios mas altos
    nsmallestPrices= df.nsmallest(5,'price')
    print(nsmallestPrices) #Imprimimos los 5 productos ocn los precios mas altos
    

#Funcion para guardar los datos entra el df y donde queremos que se guarde,limpia y graba los datos
#@logit #Añadimos el loggin a la funcion
#@timeit #Medimos el tiempo de ejecudciòn de uan funcion
def save_clean_data(df,outputh_path):
    #Guardamos los datos en un archivo .CSV
    
    if (outputh_path.endswith(".csv")):
        df.to_csv(outputh_path,index=False)#Guardamos los datos en un archivo .csv
    elif outputh_path.endswith(".xlsx"):
        df.to_excel(outputh_path,index=False)#Guardamos en un archivo excel
    else:
        raise ValueError("Unsopported file format")#lanzamos un error si el formato del archivo no es compatible
    print(f"Clean data saved to {outputh_path}")

#despues de las funciones definicmos lo sigueitne

#if __name__ == "_main_" : #Permitimos que el script se ejecute solo en este archivo 
data_path = "data/raw/products.csv" #Es la ruta del archivo de datos a procesar
outputh_path = "data/processed/cleaned_products.csv"#Definos la ruta del archivo de datos procesados
df = load_data(data_path) #Cargamos el archivo csv
print(df)
df = clean_data(df) #limpiamos los datos cargados
analyze_data(df) #Realizamos un analisis basico de la data 
os.makedirs("/data/processed",exist_ok=True) #Creamos el directorio para los datos procesados que no existe

   
save_clean_data(df,outputh_path) #limpia y graba el archivo de salida
      
    
    
    