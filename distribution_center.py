from typing import List
from utils.utils import handle_exceptions, get_user_input, display_options, validate_id, get_liters_quantity

class DistributionCenter:
    def __init__(self, id, reserve_capacity, current_reserve, daily_consumption):
        self.id = id
        self.reserve_capacity = reserve_capacity
        self.current_reserve = current_reserve
        self.daily_consumption = daily_consumption
        self.received_water = 0

distribution_centers: List[DistributionCenter] = []

@handle_exceptions
def add_center():
    while True:
        id = validate_id(distribution_centers, "Ingrese el identificador del centro de distribución o")
        if id is None:
            return
        reserve_capacity = get_liters_quantity("Ingrese la capacidad de reserva o")
        if reserve_capacity is None:
            return
        current_reserve = get_liters_quantity("Ingrese la reserva actual o", max_value=reserve_capacity)
        if current_reserve is None:
            return
        daily_consumption = get_liters_quantity("Ingrese el consumo diario o")
        if daily_consumption is None:
            return

        center = DistributionCenter(id, reserve_capacity, current_reserve, daily_consumption)
        distribution_centers.append(center)
        print("Centro de distribución agregado correctamente.")

        add_another_center = get_user_input("¿Desea introducir otro centro de distribución? (s/n): ", ['s', 'n'])
        if add_another_center.lower() != 's':
            break

@handle_exceptions
def update_center():
    print("\nModificar centro de distribución:")
    print("1) Ingresar identificador del centro de distribución a modificar")
    print("2) Listar todos los centros de distribución")
    print("0) Regresar")
    option = get_user_input("Ingrese una opción: ", ["0", "1", "2"])

    if option == "0":
        return
    elif option == "1":
        id = validate_id(distribution_centers, "Ingrese el identificador del centro de distribución a modificar o", must_exist=True)
        if id is None:
            return
    elif option == "2":
        if not distribution_centers:
            print("No hay centros de distribución dados de alta.")
            return
        center = display_options(distribution_centers, "Seleccione un centro de distribución:")
        if center is None:
            print("No se seleccionó ningún centro de distribución.")
            return
        id = center.id

    selected_center = next((centro for centro in distribution_centers if centro.id == id), None)

    if selected_center is not None:
        print("\nCentro encontrado.")
        print("1) Modificar centro")
        print("2) Dar de baja centro")
        print("0) Regresar")
        option = get_user_input("Ingrese una opción: ", ["0", "1", "2"])

        if option == "0":
            return
        elif option == "1":
            new_liters_capacity = get_liters_quantity("Ingrese la nueva capacidad de reserva o")
            if new_liters_capacity is None:
                return
            new_current_reserve = get_liters_quantity("Ingrese la nueva reserva actual o", max_value=new_liters_capacity)
            if new_current_reserve is None:
                return
            new_daily_consumption = get_liters_quantity("Ingrese el nuevo consumo diario o")
            if new_daily_consumption is None:
                return

            selected_center.reserve_capacity = new_liters_capacity
            selected_center.current_reserve = new_current_reserve
            selected_center.daily_consumption = new_daily_consumption

            print("Centro de distribución modificado correctamente.")
        elif option == "2":
            distribution_centers.remove(selected_center)
            print("Centro de distribución dado de baja correctamente.")
    else:
        print("Centro no encontrado.")

@handle_exceptions
def centers_menu():
    while True:
        print("\nCentros de distribución:")
        print("1) Alta")
        print("2) Modificación")
        print("0) Regresar")
        option = get_user_input("Ingrese una opción: ", ["0", "1", "2"])

        if option == "1":
            add_center()
        elif option == "2":
            update_center()
        elif option == "0":
            break
        else:
            print("Opción inválida. Intente de nuevo.")