import glob
import pickle
from utils.utils import get_file_name, display_options
from system import load_system_data, save_system_data

def load_data():
    files = glob.glob("data/*.pkl")
    if not files:
        print("No hay archivos disponibles.")
        return

    class File:
        def __init__(self, id):
            self.id = id

    files = [File(f) for f in files]
    file = display_options(files, "Seleccione un archivo:")

    if file is None:
        print("Operación cancelada.")
        return

    file_name = file.id

    try:
        with open(file_name, 'rb') as archivo:
            data = pickle.load(archivo)
            load_system_data(data)
            print("Datos cargados correctamente.")
    except FileNotFoundError:
        print(f"El archivo '{file_name}' no fue encontrado.")
    except Exception as e:
        print(f"Ocurrió un error al cargar los datos: {e}")

import os

def save_data():
    file_name = get_file_name("Ingrese el nombre del archivo para guardar los datos: ")
    directory = "data"
    if not os.path.exists(directory):
        os.makedirs(directory)
    file_name = f"{directory}/{file_name}"
    try:
        with open(file_name, 'wb') as archivo:
            data = save_system_data()
            pickle.dump(data, archivo)
            print("Datos guardados correctamente.")
    except Exception as e:
        print(f"Ocurrió un error al guardar los datos: {e}")