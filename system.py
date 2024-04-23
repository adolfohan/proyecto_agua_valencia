import water_source
import water_treatment_plant
import distribution_center
import interconnection

def show_system_info():
    print("\nInformación del sistema:")

    print("\nFuentes hídricas:")
    for ws in water_source.water_sources:
        print(f"- {ws.id}: {ws.quality.name}, {ws.liters_amount} litros/día")

    print("\nPlantas potabilizadoras:")
    for plant in water_treatment_plant.water_treatment_plants:
        print(f"- {plant.id}: {plant.eficiency.name}, {plant.max_liters_capacity} litros/día")

    print("\nCentros de distribución:")
    for center in distribution_center.distribution_centers:
        print(f"- {center.id}: Capacidad {center.reserve_capacity}, Reserva {center.current_reserve}, Consumo {center.daily_consumption} litros/día")

    print("\nInterconexiones:")
    for inter in interconnection.interconnections_list:
        print(f"- {inter.id}: {inter.source.id} -> {inter.target.id} ({inter.percentage}%)")

def load_system_data(data):
    try:
        water_source.water_sources, water_treatment_plant.water_treatment_plants, distribution_center.distribution_centers, interconnection.interconnections_list = data
    except Exception as e:
        print(f"An error occurred while loading the system state: {e}")

def save_system_data():
    try:
        data = (water_source.water_sources, water_treatment_plant.water_treatment_plants, distribution_center.distribution_centers, interconnection.interconnections_list)
        return data
    except Exception as e:
        print(f"An error occurred while saving the system state: {e}")