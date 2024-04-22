from typing import List
from utils import seleccionar_elemento, validar_identificador, obtener_cantidad_litros

class CentroDistribucion:
    def __init__(self, identificador, capacidad_reserva, reserva_actual, consumo_diario):
        self.identificador = identificador
        self.capacidad_reserva = capacidad_reserva
        self.reserva_actual = reserva_actual
        self.consumo_diario = consumo_diario
        self.agua_recibida = 0

centros: List[CentroDistribucion] = []

def alta_centro():
    while True:
        try:
            identificador = validar_identificador(centros, "Ingrese el identificador del centro de distribución o")
            if identificador is None:
                return
            capacidad_reserva = obtener_cantidad_litros("Ingrese la capacidad de reserva o")
            if capacidad_reserva is None:
                return
            reserva_actual = obtener_cantidad_litros("Ingrese la reserva actual o", max_value=capacidad_reserva)
            if reserva_actual is None:
                return
            consumo_diario = obtener_cantidad_litros("Ingrese el consumo diario o")
            if consumo_diario is None:
                return

            centro = CentroDistribucion(identificador, capacidad_reserva, reserva_actual, consumo_diario)
            centros.append(centro)
            print("Centro de distribución agregado correctamente.")

            opcion = input("¿Desea introducir otro centro de distribución? (s/n): ")
            if opcion.lower() != 's':
                break
        except ValueError as e:
            print(f"Error: {str(e)}")

def modificar_centro():
    try:
        print("\nModificar centro de distribución:")
        print("1) Ingresar identificador del centro de distribución a modificar")
        print("2) Listar todos los centros de distribución")
        print("0) Regresar")
        opcion = input("Ingrese una opción: ")

        while opcion not in ["0", "1", "2"]:
            print("Opción inválida. Por favor, intente de nuevo.")
            opcion = input("Ingrese una opción: ")

        if opcion == "0":
            return
        elif opcion == "1":
            identificador = validar_identificador(centros, "Ingrese el identificador del centro de distribución a modificar o", debe_existir=True)
            if identificador is None:
                return
        elif opcion == "2":
            if not centros:
                print("No hay centros de distribución dados de alta.")
                return
            centro = seleccionar_elemento(centros, "Seleccione un centro de distribución:")
            if centro is None:
                print("No se seleccionó ningún centro de distribucióna.")
                return
            identificador = centro.identificador
            print(centro.identificador)
            print("")

        centro_encontrado = None

        for centro in centros:
            if centro.identificador == identificador:
                centro_encontrado = centro
                break

        if centro_encontrado is not None:
            print("Centro encontrado.")
            print("1) Modificar centro")
            print("2) Dar de baja centro")
            print("0) Regresar")
            opcion = input("Ingrese una opción: ")

            while opcion not in ["0", "1", "2"]:
                print("Opción inválida. Por favor, intente de nuevo.")
                opcion = input("Ingrese una opción: ")

            if opcion == "0":
                return
            elif opcion == "1":
                capacidad_reserva = obtener_cantidad_litros("Ingrese la nueva capacidad de reserva o")
                if capacidad_reserva is None:
                    return
                reserva_actual = obtener_cantidad_litros("Ingrese la nueva reserva actual o", max_value=capacidad_reserva)
                if reserva_actual is None:
                    return
                consumo_diario = obtener_cantidad_litros("Ingrese el nuevo consumo diario o")
                if consumo_diario is None:
                    return

                centro_encontrado.capacidad_reserva = capacidad_reserva
                centro_encontrado.reserva_actual = reserva_actual
                centro_encontrado.consumo_diario = consumo_diario

                print("Centro de distribución modificado correctamente.")
            elif opcion == "2":
                centros.remove(centro_encontrado)
                print("Centro de distribución dado de baja correctamente.")
        else:
            print("Centro no encontrado.")
    except Exception as e:
        print(f"Error: {str(e)}")
        
def menu_centros():
    while True:
        print("\nCentros de distribución:")
        print("1) Alta")
        print("2) Modificación")
        print("0) Regresar")

        try:
            opcion = input("Ingrese una opción: ")

            if opcion == "1":
                alta_centro()
            elif opcion == "2":
                modificar_centro()
            elif opcion == "0":
                break
            else:
                print("Opción inválida. Intente de nuevo.")
        except KeyboardInterrupt:
            print("\nPrograma interrumpido por el usuario.")
            break
        except Exception as e:
            print(f"Error: {str(e)}")