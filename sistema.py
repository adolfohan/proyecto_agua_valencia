import fuentes
import plantas
import centros
import interconexiones
import pickle

def mostrar_info_sistema():
    print("\nInformación del sistema:")

    print("\nFuentes hídricas:")
    for fuente in fuentes.fuentes:
        print(f"- {fuente.identificador}: {fuente.calidad.name}, {fuente.cantidad_litros} litros/día")

    print("\nPlantas potabilizadoras:")
    for planta in plantas.plantas:
        print(f"- {planta.identificador}: {planta.eficiencia.name}, {planta.cantidad_litros_maxima} litros/día")

    print("\nCentros de distribución:")
    for centro in centros.centros:
        print(f"- {centro.identificador}: Capacidad {centro.capacidad_reserva}, Reserva {centro.reserva_actual}, Consumo {centro.consumo_diario} litros/día")

    print("\nInterconexiones:")
    for interconexion in interconexiones.interconexiones:
        print(f"- {interconexion.identificador}: {interconexion.origen.identificador} -> {interconexion.destino.identificador} ({interconexion.porcentaje}%)")

def cargar_sistema(archivo):
    try:
        data = pickle.load(archivo)
        fuentes.fuentes, plantas.plantas, centros.centros, interconexiones.interconexiones = data
        print("System state loaded successfully.")
    except Exception as e:
        print(f"An error occurred while loading the system state: {e}")

def guardar_sistema(archivo):
    try:
        data = (fuentes.fuentes, plantas.plantas, centros.centros, interconexiones.interconexiones)
        pickle.dump(data, archivo)
        print("System state saved successfully.")
    except Exception as e:
        print(f"An error occurred while saving the system state: {e}")