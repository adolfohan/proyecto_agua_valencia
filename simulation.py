import water_source
import water_treatment_plant
import distribution_center
import interconnection
from utils.utils import get_number_of_days

def purify_water(plant, water_quantity):
    efficiency_correction = 1.0
    if plant.eficiency == water_treatment_plant.Eficiency.MEDIA:
        efficiency_correction -= 0.1
    elif plant.eficiency == water_treatment_plant.Eficiency.BAJA:
        efficiency_correction -= 0.2
    
    for inter in interconnection.interconnections_list:
        if inter.target == plant:
            ws = inter.source
            if ws.quality == water_source.Quality.POTABLE:
                return water_quantity
            elif ws.quality == water_source.Quality.MEDIA:
                efficiency_correction -= 0.1
            elif ws.quality == water_source.Quality.BAJA:
                efficiency_correction -= 0.2
            elif ws.quality == water_source.Quality.NOPOTABILIZABLE:
                return 0

    return water_quantity * efficiency_correction

def simulate_days():
    try:
        simulation_days = get_number_of_days("Ingrese la cantidad de días a simular o")
        if simulation_days is None:
            print("Simulación cancelada.")
            return
        elif simulation_days <= 0:
            print("La cantidad de días debe ser mayor a cero.")
            return
    except ValueError:
        print("La cantidad de días ingresada no es válida.")
        return

    for day in range(1, simulation_days + 1):
        print(f"\nDía {day}:")

        # 1) Fuentes entregan agua a las plantas potabilizadoras con las que tengan interconexión
        for inter in interconnection.interconnections_list:
            if isinstance(inter.source, water_source.WaterSource) and isinstance(inter.target, water_treatment_plant.WaterTreatmentPlant):
                ws = inter.source
                plant = inter.target
                water_delivered_amount = ws.liters_amount * (inter.percentage / 100)
                plant.received_water = water_delivered_amount
                print(f"La fuente {ws.id} entregó {water_delivered_amount} litros a la planta {plant.id}")

        # 2) Plantas potabilizadoras potabilizan agua según parámetros
        for plant in water_treatment_plant.water_treatment_plants:
            if not any(inter.source == plant for inter in interconnection.interconnections_list):
                continue
            if isinstance(plant, water_treatment_plant.WaterTreatmentPlant):
                plant.water_treated = purify_water(plant, plant.received_water)
                print(f"La planta {plant.id} potabilizó {plant.water_treated} litros de agua")
            else:
                print(f"Error: se encontró un objeto que no es una PlantaPotabilizadora en la lista 'plantas'. Tipo de objeto: {type(plant)}")

        # 3) Plantas potabilizadoras entregan agua a los centros de distribución según parámetros indicados
        for inter in interconnection.interconnections_list:
            if isinstance(inter.source, water_treatment_plant.WaterTreatmentPlant) and isinstance(inter.target, distribution_center.DistributionCenter):
                plant = inter.source
                center = inter.target
                water_delivered_amount = plant.water_treated * (inter.percentage / 100)
                center.received_water += water_delivered_amount
                print(f"La planta {plant.id} entregó {water_delivered_amount} litros de agua al centro {center.id}")

        # 4) Centros de distribución consumen agua
        for center in distribution_center.distribution_centers:
            if not any(inter.target == center for inter in interconnection.interconnections_list):
                continue
            center.current_reserve += center.received_water
            center.current_reserve -= center.daily_consumption
            center.received_water = 0
            print(f"El centro {center.id} consumió {center.daily_consumption} litros de agua")

        # 5) Cierre día. Se corrigen posibles desbordes "temporales"
        for center in distribution_center.distribution_centers:
            if not any(inter.target == center for inter in interconnection.interconnections_list):
                continue
            if center.current_reserve > center.reserve_capacity:
                center.current_reserve = center.reserve_capacity
            print(f"El centro {center.id} tiene {center.current_reserve} litros de agua en reserva al final del día")

    print("\nSimulación finalizada.")