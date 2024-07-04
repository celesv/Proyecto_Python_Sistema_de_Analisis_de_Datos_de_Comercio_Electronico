import time # Importar el modulo time para medir el tiempo de ejecución
import logging # Importar el modulo logging para registrar mensajes


# Confirguramos el logger 

logging.basicConfig(level=logging.INFO, format = "%(asctime)s - %(levelname)s - %(message)s")

# Configuramos el registro de mensajes (LOGGING) para que muestre mensajes de nivel INFO y superior.
# Definimos el formato de los mensajes de registro, incluyendo la marca de tiempo (asctime), el nivel de mensaje (levelname), y el mensaje (message).


def timeit(func):
    """Decorador para medir el tiempo de ejecucion de una funcion"""
    def wrapper(*args, **kwargs):   
        start_time = time.time() # Registramos el tiempo de inicio de la ejecucion
        result = func(*args, **kwargs) # Ejecutamos la funcion que recibimos como argumento, es decir, la función decoradora
        end_time = time.time() # Registramos el tiempo de fin de la ejecucion
        elapsed_time = end_time - start_time # Calculamos el tiempo de ejecucion
        logging.info(f"La función {func.__name__} ha tardado {elapsed_time} segundos") # Imprimimos el tiempo de ejecucion de la funcion
        return result # Devolvemos el resultado de la ejecucion de la funcion
    return wrapper


def logit(func):
    """Decorador para registrar la de ejecucion de una funcion"""
    def wrapper(*args, **kwargs):
        logging.info(f"La función {func.__name__} ha sido llamada") # Registramos el inicio de la ejecucion de la funcion
        result = func(*args, **kwargs) # Ejecutamos la funcion que recibimos como argumento, es decir, la función decoradora
        logging.info(f"La función {func.__name__} ha terminado") # Registramos el fin de la ejecucion de la funcion
        return result # Devolvemos el resultado de la ejecucion de la funcion
    return wrapper
