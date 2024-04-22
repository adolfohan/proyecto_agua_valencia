import fuente_hidrica
import planta_potabilizadora
import centro_distribucion
import interconexion

def mostrar_info_sistema():
    print("\nInformación del sistema:")

    print("\nFuentes hídricas:")
    for fuente in fuente_hidrica.fuentes:
        print(f"- {fuente.identificador}: {fuente.calidad.name}, {fuente.cantidad_litros} litros/día")

    print("\nPlantas potabilizadoras:")
    for planta in planta_potabilizadora.plantas:
        print(f"- {planta.identificador}: {planta.eficiencia.name}, {planta.cantidad_litros_maxima} litros/día")

    print("\nCentros de distribución:")
    for centro in centro_distribucion.centros:
        print(f"- {centro.identificador}: Capacidad {centro.capacidad_reserva}, Reserva {centro.reserva_actual}, Consumo {centro.consumo_diario} litros/día")

    print("\nInterconexiones:")
    for inter in interconexion.interconexiones_list:
        print(f"- {inter.identificador}: {inter.origen.identificador} -> {inter.destino.identificador} ({inter.porcentaje}%)")

def cargar_sistema(data):
    try:
        fuente_hidrica.fuentes, planta_potabilizadora.plantas, centro_distribucion.centros, interconexion.interconexiones_list = data
    except Exception as e:
        print(f"An error occurred while loading the system state: {e}")

def guardar_sistema():
    try:
        data = (fuente_hidrica.fuentes, planta_potabilizadora.plantas, centro_distribucion.centros, interconexion.interconexiones_list)
        return data
    except Exception as e:
        print(f"An error occurred while saving the system state: {e}")