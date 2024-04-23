import itertools
from typing import List
import water_source
import water_treatment_plant
import distribution_center
from utils.utils import handle_exceptions, get_user_input, validate_percentage, display_options

class Interconnection:
    counter = itertools.count(1)

    def __init__(self, source, target, percentage):
        self.id = self.generate_id(source, target)
        self.source = source
        self.target = target
        self.percentage = percentage
    
    def generate_id(self, source, target):
        return f"{source.id}-{target.id}-{next(self.counter)}"

interconnections_list: List[Interconnection] = []

def get_available_element(elements, message):
    print(message)
    available_elements = [element for element in elements if element.can_add_interconnection()]
    for i, element in enumerate(available_elements, start=1):
        print(f"{i}) {element.id}")

    option = input("Ingrese el número correspondiente o 'cancelar' para volver atrás: ")

    if option.lower() == 'cancelar':
        return None

    try:
        index = int(option) - 1
        return available_elements[index]
    except (ValueError, IndexError):
        print("Opción inválida.")
        return None

@handle_exceptions
def add_interconnection():
    print("\nAlta de interconexión:")
    print("1) Fuente hídrica")
    print("2) Planta potabilizadora")
    print("0) Regresar")
    
    options = ["1", "2", "0"]
    option = get_user_input("Seleccione el tipo de origen: ", options, "0")

    if option == "0":
        return
    elif option == "1":
        source = get_available_element(water_source.water_sources, "Seleccione una fuente hídrica: ")
        if source is None:
            return
        target = display_options(water_treatment_plant.water_treatment_plants, "Seleccione una planta potabilizadora: ")
        if target is None:
            return
    elif option == "2":
        source = get_available_element(water_treatment_plant.water_treatment_plants, "Seleccione una planta potabilizadora: ")
        if source is None:
            return
        target = display_options(distribution_center.distribution_centers, "Seleccione un centro de distribución: ")
        if target is None:
            return
    else:
        print("Opción inválida.")
        return


    if source is None or target is None:
        return
    
    if not hasattr(source, 'id') or not hasattr(target, 'id'):
        print("Origen o destino no tienen un identificador.")
        return

    while True:
        try:
            percentage = float(input("Ingrese el porcentaje de la interconexión: "))
            if percentage <= 0 or percentage > 100:
                print("Porcentaje inválido. Debe ser mayor que 0 y menor o igual a 100.")
            else:
                break
        except ValueError:
            print("Por favor, ingrese un número.")

    if not source.can_add_interconnection(percentage):
        print("La capacidad asignada supera el 100% con las otras interconexiones existentes.")
        return
    
    total_percentage = sum(i.percentage for i in interconnections_list if i.source == source)
    if total_percentage + percentage > 100:
        print("La capacidad asignada supera el 100% con las otras interconexiones existentes.")
        return

    interconnection = Interconnection(source, target, percentage)
    interconnection.id = f"{source.id}-{target.id}-{len(interconnections_list) + 1}"
    interconnections_list.append(interconnection)
    print("Interconexión agregada correctamente.")

@handle_exceptions
def update_interconnection():
    print("\nModificar interconexión:")
    print("1) Ingresar identificador de la interconexión a modificar")
    print("2) Listar todas las interconexiones")
    print("0) Regresar")
    
    options = ["1", "2", "0"]
    option = get_user_input("Ingrese una opción: ", options, "0")

    if option == "0":
        return
    elif option == "1":
        id = input("Ingrese el identificador de la interconexión a modificar o")
        if id.lower() == 'cancelar':
            return None
    elif option == "2":
        if not interconnections_list:
            print("No hay interconexiones dadas de alta.")
            return
        interconnection = display_options(interconnections_list, "Seleccione una interconexión:")
        if interconnection is None:
            return
        id = interconnection.id
        print(interconnection.id)
        print("")

    interconnection = next((i for i in interconnections_list if i.id == id), None)
    if interconnection is None:
        print(f"No se encontró una interconexión con el identificador '{id}'.")
        return

    print("\nInterconexión encontrada.")
    print("1) Modificar interconexión")
    print("2) Dar de baja interconexión")
    print("0) Regresar")
    option = input("Ingrese una opción: ")

    while option not in ["0", "1", "2"]:
        print("Opción inválida. Por favor, intente de nuevo.")
        option = input("Ingrese una opción: ")

    if option == "0":
        return
    elif option == "1":
        new_percentage = validate_percentage("Ingrese el nuevo porcentaje de la interconexión o")
        if new_percentage is None:
            return None

        interconnection.percentage = new_percentage
        print("Interconexión modificada correctamente.")
    elif option == "2":
        interconnections_list.remove(interconnection)
        print("Interconexión dada de baja correctamente.")

@handle_exceptions
def interconnection_menu():
    while True:
        print("\nInterconexiones:")
        print("1) Alta")
        print("2) Modificación")
        print("0) Regresar")

        options = ["1", "2", "0"]
        option = get_user_input("Ingrese una opción: ", options, "0")

        if option == "1":
            add_interconnection()
        elif option == "2":
            update_interconnection()
        elif option == "0":
            break
        else:
            print("Opción inválida. Intente de nuevo.")