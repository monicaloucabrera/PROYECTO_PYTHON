import time #importamos el modulo time para medir el tiempo de ejecucion
import logging #importamos el modulo logging para registrar mensajes


#configuramos el logger

logging.basicConfig(level=logging.INFO,format="%(asctime)s - %(levelname)s- % (message)s")

    #Configuramos el registro de mensajes (LOGGING) para que muestre mensajes de tipo INFO y superior
    #Definimos el formato de los mensjes de registro, incluyendo la marca del tiempo(asctime),
    #el nivel e menssje(levelname) y el mensaje (message)
    
def timeit(func):
    #Decorador para medir el tiempo de jecucion de una funcion
     def wrapper(*args, **kwargs):
         start_time = time.time() #registramos el tiempo de inicio
         
         result = func(*args,**kwargs) #ejecutamos la funcion decoradora
         end_time = time.time() #Registramos el tiempo de finalizacion
         elapsed_time = end_time - start_time #calculamos el tiempo transcurrido
         logging.info(f"{func.__name__} ejecutada en {elapsed_time:.4f} seconds\n")#Registramos el tiempo de ejecucion
         return result #Retornamos el tiempo de ejecucion
     return wrapper #Devolvemos el decorador
 
def logit(func):
    #Decorador para regstrar la ejecucion de una funcion
    def wrapper(*args, **kwargs):
        logging.info(f"Corriendo {func.__name__}\n") #Registramos el inicio de la ejecucion
        result = func(*args,**kwargs)
        logging.info(f"Completaod {func.__name__}\n") #Registramos la finalizacion de la ejecucion de la funcion
        return result #decolvemos el resultado de la funcion
    return wrapper

     
    
    
    
    
    
