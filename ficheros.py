from utils import obtener_nombre_archivo
from sistema import cargar_sistema, guardar_sistema

def cargar_datos():
    nombre_archivo = obtener_nombre_archivo("Ingrese el nombre del archivo para cargar los datos: ")
    try:
        with open(nombre_archivo, 'rb') as archivo:
            cargar_sistema(archivo)
            print("Datos cargados correctamente.")
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no fue encontrado.")
    except Exception as e:
        print(f"Ocurrió un error al cargar los datos: {e}")

def guardar_datos():
    nombre_archivo = obtener_nombre_archivo("Ingrese el nombre del archivo para guardar los datos: ")
    try:
        with open(nombre_archivo, 'wb') as archivo:
            guardar_sistema(archivo)
            print("Datos guardados correctamente.")
    except Exception as e:
        print(f"Ocurrió un error al guardar los datos: {e}")