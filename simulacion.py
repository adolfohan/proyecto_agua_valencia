from fuentes import FuenteHidrica
from plantas import plantas, PlantaPotabilizadora, Eficiencia
from centros import CentroDistribucion, centros
from interconexiones import interconexiones
from utils import obtener_cantidad_dias

def potabilizar_agua(planta, cantidad_agua):
    factor_correccion = 1.0
    if planta.eficiencia == Eficiencia.MEDIA:
        factor_correccion -= 0.1
    elif planta.eficiencia == Eficiencia.BAJA:
        factor_correccion -= 0.2

    for interconexion in interconexiones:
        if interconexion.destino == planta:
            fuente = interconexion.origen
            if fuente.calidad == "Media":
                factor_correccion -= 0.1
            elif fuente.calidad == "Baja":
                factor_correccion -= 0.2
            elif fuente.calidad == "NoPotabilizable":
                return 0

    return cantidad_agua * factor_correccion

def simular_dias():
    try:
        cantidad_dias = obtener_cantidad_dias("Ingrese la cantidad de días a simular: ")
        if cantidad_dias <= 0:
            print("La cantidad de días debe ser mayor a cero.")
            return
    except ValueError:
        print("La cantidad de días ingresada no es válida.")
        return

    for dia in range(1, cantidad_dias + 1):
        print(f"\nDía {dia}:")

        # 1) Fuentes entregan agua a las plantas potabilizadoras con las que tengan interconexión
        for interconexion in interconexiones:
            if isinstance(interconexion.origen, FuenteHidrica) and isinstance(interconexion.destino, PlantaPotabilizadora):
                fuente = interconexion.origen
                planta = interconexion.destino
                cantidad_agua_entregada = fuente.cantidad_litros * (interconexion.porcentaje / 100)
                planta.agua_recibida = cantidad_agua_entregada
                print(f"La fuente {fuente.identificador} entregó {cantidad_agua_entregada} litros a la planta {planta.identificador}")

        # 2) Plantas potabilizadoras potabilizan agua según parámetros
        for planta in plantas:
            if isinstance(planta, PlantaPotabilizadora):
                planta.agua_potabilizada = potabilizar_agua(planta, planta.agua_recibida)
                print(f"La planta {planta.identificador} potabilizó {planta.agua_potabilizada} litros de agua")
            else:
                print(f"Error: se encontró un objeto que no es una PlantaPotabilizadora en la lista 'plantas'. Tipo de objeto: {type(planta)}")

        # 3) Plantas potabilizadoras entregan agua a los centros de distribución según parámetros indicados
        for interconexion in interconexiones:
            if isinstance(interconexion.origen, PlantaPotabilizadora) and isinstance(interconexion.destino, CentroDistribucion):
                planta = interconexion.origen
                centro = interconexion.destino
                cantidad_agua_entregada = planta.agua_potabilizada * (interconexion.porcentaje / 100)
                centro.agua_recibida += cantidad_agua_entregada
                print(f"La planta {planta.identificador} entregó {cantidad_agua_entregada} litros de agua al centro {centro.identificador}")

        # 4) Centros de distribución consumen agua
        for centro in centros:
            centro.reserva_actual -= centro.consumo_diario
            centro.agua_recibida = 0
            print(f"El centro {centro.identificador} consumió {centro.consumo_diario} litros de agua")

        # 5) Cierre día. Se corrigen posibles desbordes "temporales"
        for centro in centros:
            if centro.reserva_actual > centro.capacidad_reserva:
                centro.reserva_actual = centro.capacidad_reserva
        print(f"El centro {centro.identificador} tiene {centro.reserva_actual} litros de agua en reserva al final del día")

    print("\nSimulación finalizada.")