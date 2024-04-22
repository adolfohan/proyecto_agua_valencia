import fuente_hidrica #import FuenteHidrica, Calidad
import planta_potabilizadora #import plantas, PlantaPotabilizadora, Eficiencia
import centro_distribucion #import CentroDistribucion, centros
import interconexion #import interconexiones_list
from utils import obtener_cantidad_dias

def potabilizar_agua(planta, cantidad_agua):
    factor_correccion = 1.0
    if planta.eficiencia == planta_potabilizadora.Eficiencia.MEDIA:
        factor_correccion -= 0.1
    elif planta.eficiencia == planta_potabilizadora.Eficiencia.BAJA:
        factor_correccion -= 0.2

    for inter in interconexion.interconexiones_list:
        if inter.destino == planta:
            fuente = inter.origen
            if fuente.calidad == fuente_hidrica.Calidad.MEDIA:
                factor_correccion -= 0.1
            elif fuente.calidad == fuente_hidrica.Calidad.BAJA:
                factor_correccion -= 0.2
            elif fuente.calidad == fuente_hidrica.Calidad.NOPOTABILIZABLE:
                return 0

    return cantidad_agua * factor_correccion

def simular_dias():
    try:
        cantidad_dias = obtener_cantidad_dias("Ingrese la cantidad de días a simular o")
        if cantidad_dias <= 0:
            print("La cantidad de días debe ser mayor a cero.")
            return
    except ValueError:
        print("La cantidad de días ingresada no es válida.")
        return

    for dia in range(1, cantidad_dias + 1):
        print(f"\nDía {dia}:")

        # 1) Fuentes entregan agua a las plantas potabilizadoras con las que tengan interconexión
        for inter in interconexion.interconexiones_list:
            if isinstance(inter.origen, fuente_hidrica.FuenteHidrica) and isinstance(inter.destino, planta_potabilizadora.PlantaPotabilizadora):
                fuente = inter.origen
                planta = inter.destino
                cantidad_agua_entregada = fuente.cantidad_litros * (inter.porcentaje / 100)
                planta.agua_recibida = cantidad_agua_entregada
                print(f"La fuente {fuente.identificador} entregó {cantidad_agua_entregada} litros a la planta {planta.identificador}")

        # 2) Plantas potabilizadoras potabilizan agua según parámetros
        for planta in planta_potabilizadora.plantas:
            if not any(inter.origen == planta for inter in interconexion.interconexiones_list):
                continue
            if isinstance(planta, planta_potabilizadora.PlantaPotabilizadora):
                planta.agua_potabilizada = potabilizar_agua(planta, planta.agua_recibida)
                print(f"La planta {planta.identificador} potabilizó {planta.agua_potabilizada} litros de agua")
            else:
                print(f"Error: se encontró un objeto que no es una PlantaPotabilizadora en la lista 'plantas'. Tipo de objeto: {type(planta)}")

        # 3) Plantas potabilizadoras entregan agua a los centros de distribución según parámetros indicados
        for inter in interconexion.interconexiones_list:
            if isinstance(inter.origen, planta_potabilizadora.PlantaPotabilizadora) and isinstance(inter.destino, centro_distribucion.CentroDistribucion):
                planta = inter.origen
                centro = inter.destino
                cantidad_agua_entregada = planta.agua_potabilizada * (inter.porcentaje / 100)
                centro.agua_recibida += cantidad_agua_entregada
                print(f"La planta {planta.identificador} entregó {cantidad_agua_entregada} litros de agua al centro {centro.identificador}")

        # 4) Centros de distribución consumen agua
        for centro in centro_distribucion.centros:
            if not any(inter.destino == centro for inter in interconexion.interconexiones_list):
                continue
            centro.reserva_actual += centro.agua_recibida
            centro.reserva_actual -= centro.consumo_diario
            centro.agua_recibida = 0
            print(f"El centro {centro.identificador} consumió {centro.consumo_diario} litros de agua")

        # 5) Cierre día. Se corrigen posibles desbordes "temporales"
        for centro in centro_distribucion.centros:
            if not any(inter.destino == centro for inter in interconexion.interconexiones_list):
                continue
            if centro.reserva_actual > centro.capacidad_reserva:
                centro.reserva_actual = centro.capacidad_reserva
            print(f"El centro {centro.identificador} tiene {centro.reserva_actual} litros de agua en reserva al final del día")

    print("\nSimulación finalizada.")