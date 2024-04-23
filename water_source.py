from typing import List
from enums.enumQuality import Quality
from utils.utils import handle_exceptions, get_user_input, display_options, validate_id, get_water_quality, get_liters_quantity

class WaterSource:
    def __init__(self, id, quality, liters_amount):
        self.id = id
        if quality not in Quality:
            raise ValueError("La calidad proporcionada no es válida.")
        self.quality = quality
        self.liters_amount = liters_amount
        self.assigned_capacity = 0
    
    def can_add_interconnection(self, percentage=None):
        if percentage is None:
            return self.assigned_capacity < self.liters_amount
        else:
            return self.assigned_capacity + (percentage / 100.0) * self.liters_amount <= self.liters_amount

water_sources: List[WaterSource] = []

@handle_exceptions
def add_water_source():
    while True:
        id = validate_id(water_sources, "Ingrese el identificador de la fuente hídrica o")
        if id is None:
            return
        
        water_quality = get_water_quality("Ingrese la calidad del agua o")
        if water_quality is None:
            return
        liters_per_day = get_liters_quantity("Ingrese la cantidad de litros por día o")
        if liters_per_day is None:
            return

        water_source = WaterSource(id, water_quality, liters_per_day)
        water_sources.append(water_source)
        print("Fuente hídrica agregada correctamente.")

        while True:
            add_another_source = input("¿Desea agregar otra fuente hídrica? (s/n): ")
            if add_another_source.lower() in ['s', 'n']:
                break
            else:
                print("Opción inválida. Por favor, ingrese 's' o 'n'.")

        if add_another_source.lower() != 's':
            break

@handle_exceptions
def update_water_source():
    print("\nModificar fuente hídrica:")
    print("1) Ingresar identificador de la fuente hídrica a modificar")
    print("2) Listar todas las fuentes hídricas")
    print("0) Regresar")
    option = input("Ingrese una opción: ")

    while option not in ["0", "1", "2"]:
        print("Opción inválida. Por favor, intente de nuevo.")
        option = input("Ingrese una opción: ")

    if option == "0":
        return
    elif option == "1":
        id = validate_id(water_sources, "Ingrese el identificador de la fuente hídrica a modificar o", must_exist=True)
        if id is None:
            return
    elif option == "2":
        if not water_sources:
            print("No hay fuentes hídricas dadas de alta.")
            return
        water_source = display_options(water_sources, "Seleccione una fuente hídrica:")
        if water_source is None:
            return
        id = water_source.id
        print(water_source.id)
        print("")

    for water_source in water_sources:
        if water_source.id == id:
            print("\n1) Cambiar información")
            print("2) Dar de baja")
            print("0) Regresar")
            option = input("Ingrese una opción: ")

            while option not in ["0", "1", "2"]:
                print("Opción inválida. Por favor, intente de nuevo.")
                option = input("Ingrese una opción: ")

            if option == "0":
                return
            elif option == "1":
                new_water_quality = get_water_quality("Ingrese la nueva calidad del agua o")
                if new_water_quality is None:
                    return
                new_liters_per_day = get_liters_quantity("Ingrese la nueva cantidad de litros por día o")
                if new_liters_per_day is None:
                    return
                water_source.water_quality = new_water_quality
                water_source.liters_amount = new_liters_per_day
                print("Fuente hídrica modificada correctamente.")
            elif option == "2":
                water_sources.remove(water_source)
                print("Fuente hídrica dada de baja correctamente.")
            break
    else:
        print("No se encontró una fuente hídrica con el identificador ingresado.")

@handle_exceptions
def water_sources_menu():
    while True:
        print("\nFuentes hídricas:")
        print("1) Alta")
        print("2) Modificación")
        print("0) Regresar")

        option = get_user_input("Ingrese una opción: ", ["1", "2", "0"])

        if option == "1":
            add_water_source()
        elif option == "2":
            update_water_source()
        elif option == "0":
            break