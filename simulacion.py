from fuentes import fuentes, FuenteHidrica
from plantas import plantas, PlantaPotabilizadora, Eficiencia
from centros import centros
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
            if isinstance(interconexion.origen, FuenteHidrica):
                fuente = interconexion.origen
                planta = interconexion.destino
                cantidad_agua_entregada = fuente.cantidad_litros * (interconexion.porcentaje / 100)
                planta.agua_recibida = cantidad_agua_entregada

        # 2) Plantas potabilizadoras potabilizan agua según parámetros
        for planta in plantas:
            planta.agua_potabilizada = potabilizar_agua(planta, planta.agua_recibida)

        # 3) Plantas potabilizadoras entregan agua a los centros de distribución según parámetros indicados
        for interconexion in interconexiones:
            if isinstance(interconexion.origen, PlantaPotabilizadora):
                planta = interconexion.origen
                centro = interconexion.destino
                cantidad_agua_entregada = planta.agua_potabilizada * (interconexion.porcentaje / 100)
                centro.agua_recibida += cantidad_agua_entregada

        # 4) Centros de distribución consumen agua
        for centro in centros:
            centro.reserva_actual -= centro.consumo_diario
            centro.agua_recibida = 0

        # 5) Cierre día. Se corrigen posibles desbordes "temporales"
        for centro in centros:
            if centro.reserva_actual > centro.capacidad_reserva:
                centro.reserva_actual = centro.capacidad_reserva

    print("\nSimulación finalizada.")