from typing import List
from enums.enumEficiency import Eficiency
from utils.utils import handle_exceptions, get_user_input, display_options, validate_id, get_efficiency, get_liters_quantity

class WaterTreatmentPlant:
    def __init__(self, id, eficiency, max_liters_capacity):
        self.id = id
        if eficiency not in Eficiency:
            raise ValueError("La eficiencia proporcionada no es válida.")
        self.eficiency = eficiency
        self.max_liters_capacity = max_liters_capacity
        self.assigned_capacity = 0
        self.received_water = 0
        self.water_treated = 0
        
    def can_add_interconnection(self, percentage=None):
        if percentage is None:
            return self.assigned_capacity < self.max_liters_capacity
        else:
            return self.assigned_capacity + (percentage / 100.0) * self.max_liters_capacity <= self.max_liters_capacity

water_treatment_plants: List[WaterTreatmentPlant] = []

@handle_exceptions
def add_plant():
    while True:
        id = validate_id(water_treatment_plants, "Ingrese el identificador de la planta potabilizadora o")
        if id is None:
            return
        efficiency = get_efficiency("Ingrese la eficiencia de la planta o")
        if efficiency is None:
            return
        max_liters_quantity = get_liters_quantity("Ingrese la cantidad máxima de litros por día o")
        if max_liters_quantity is None:
            return

        plant = WaterTreatmentPlant(id, efficiency, max_liters_quantity)
        water_treatment_plants.append(plant)
        print("Planta potabilizadora agregada correctamente.")

        add_another_plant = get_user_input("¿Desea agregar otra planta potabilizadora? (s/n): ", ['s', 'n'])
        if add_another_plant.lower() != 's':
            break

@handle_exceptions
def update_plant():
    print("\nModificar planta potabilizadora:")
    print("1) Ingresar identificador de la planta potabilizadora a modificar")
    print("2) Listar todas las plantas potabilizadoras")
    print("0) Regresar")
        
    option = get_user_input("Ingrese una opción: ", ["0", "1", "2"])

    if option == "0":
        return
    elif option == "1":
        id = validate_id(water_treatment_plants, "Ingrese el identificador de la planta potabilizadora a modificar o", must_exist=True)
        if id is None:
            return
    elif option == "2":
        if not water_treatment_plants:
            print("No hay plantas potabilizadoras dadas de alta.")
            return
        plant = display_options(water_treatment_plants, "Seleccione una planta potabilizadora:")
        if plant is None:
            return
        id = plant.id

    selected_plant = next((planta for planta in water_treatment_plants if planta.id == id), None)

    if selected_plant is not None:
        print("\nPlanta encontrada.")
        print("1) Modificar planta")
        print("2) Dar de baja planta")
        print("0) Regresar")
        
        option = get_user_input("Ingrese una opción: ", ["0", "1", "2"])

        if option == "0":
            return
        elif option == "1":
            new_efficiency = get_efficiency("Ingrese la nueva eficiencia de la planta o")
            if new_efficiency is None:
                return
            new_max_liters_quantity = get_liters_quantity("Ingrese la nueva cantidad máxima de litros por día o")
            if new_max_liters_quantity is None:
                return

            selected_plant.eficiency = new_efficiency
            selected_plant.max_liters_capacity = new_max_liters_quantity

            print("Planta potabilizadora modificada correctamente.")
        elif option == "2":
            water_treatment_plants.remove(selected_plant)
            print("Planta potabilizadora dada de baja correctamente.")
    else:
        print("Planta no encontrada.")

@handle_exceptions
def plants_menu():
    while True:
        print("\nPlantas potabilizadoras:")
        print("1) Alta")
        print("2) Modificación")
        print("0) Regresar")
        
        option = get_user_input("Ingrese una opción: ", ["0", "1", "2"])

        if option == "1":
            add_plant()
        elif option == "2":
            update_plant()
        elif option == "0":
            break
        else:
            print("Opción inválida. Intente de nuevo.")