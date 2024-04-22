import itertools
from typing import List
import fuente_hidrica #import fuentes
import planta_potabilizadora #import plantas
import centro_distribucion #import centros
from utils import validar_porcentaje, seleccionar_elemento

class Interconexion:
    contador = itertools.count(1)

    def __init__(self, origen, destino, porcentaje):
        self.identificador = self.generar_identificador(origen, destino)
        self.origen = origen
        self.destino = destino
        self.porcentaje = porcentaje
    
    def generar_identificador(self, origen, destino):
        return f"{origen.identificador}-{destino.identificador}-{next(self.contador)}"

interconexiones_list: List[Interconexion] = []

def seleccionar_elemento_disponible(elementos, mensaje):
    print(mensaje)
    elementos_disponibles = [elemento for elemento in elementos if elemento.puede_agregar_interconexion()]
    for i, elemento in enumerate(elementos_disponibles, start=1):
        print(f"{i}) {elemento.identificador}")

    opcion = input("Ingrese el número correspondiente o 'cancelar' para volver atrás: ")

    if opcion.lower() == 'cancelar':
        return None

    try:
        indice = int(opcion) - 1
        return elementos_disponibles[indice]
    except (ValueError, IndexError):
        print("Opción inválida.")
        return None

def alta_interconexion():
    print("\nAlta de interconexión:")
    print("1) Fuente hídrica")
    print("2) Planta potabilizadora")
    print("0) Regresar")

    try:
        opcion = int(input("Seleccione el tipo de origen: "))
    except ValueError:
        print("Opción inválida. Debe ingresar un número.")
        return

    if opcion == 0:
        return
    elif opcion == 1:
        origen = seleccionar_elemento_disponible(fuente_hidrica.fuentes, "Seleccione una fuente hídrica: ")
        if origen is None:
            return
        destino = seleccionar_elemento(planta_potabilizadora.plantas, "Seleccione una planta potabilizadora: ")
        if destino is None:
            return
    elif opcion == 2:
        origen = seleccionar_elemento_disponible(planta_potabilizadora.plantas, "Seleccione una planta potabilizadora: ")
        if origen is None:
            return
        destino = seleccionar_elemento(centro_distribucion.centros, "Seleccione un centro de distribución: ")
        if destino is None:
            return
    else:
        print("Opción inválida.")
        return

    if origen is None or destino is None:
        return
    
    if not hasattr(origen, 'identificador') or not hasattr(destino, 'identificador'):
        print("Origen o destino no tienen un identificador.")
        return

    while True:
        try:
            porcentaje = float(input("Ingrese el porcentaje de la interconexión: "))
            if porcentaje <= 0 or porcentaje > 100:
                print("Porcentaje inválido. Debe ser mayor que 0 y menor o igual a 100.")
            else:
                break
        except ValueError:
            print("Por favor, ingrese un número.")

    if not origen.puede_agregar_interconexion(porcentaje):
        print("La capacidad asignada supera el 100% con las otras interconexiones existentes.")
        return

    interconexion = Interconexion(origen, destino, porcentaje)
    interconexion.identificador = f"{origen.identificador}-{destino.identificador}-{len(interconexiones_list) + 1}"
    interconexiones_list.append(interconexion)
    print("Interconexión agregada correctamente.")

def modificar_interconexion():
    try:
        print("\nModificar interconexión:")
        print("1) Ingresar identificador de la interconexión a modificar")
        print("2) Listar todas las interconexiones")
        print("0) Regresar")
        opcion = input("Ingrese una opción: ")

        while opcion not in ["0", "1", "2"]:
            print("Opción inválida. Por favor, intente de nuevo.")
            opcion = input("Ingrese una opción: ")

        if opcion == "0":
            return
        elif opcion == "2":
            if not interconexiones_list:
                print("No hay interconexiones dadas de alta.")
                return
            for interconexion in interconexiones_list:
                print(interconexion.identificador)
            print("")

        identificador = input("Ingrese el identificador de la interconexión a modificar o ingrese 'cancelar' para volver atrás: ")
        if identificador.lower() == 'cancelar':
            return None

        interconexion = next((i for i in interconexiones_list if i.identificador == identificador), None)
        if interconexion is None:
            print(f"No se encontró una interconexión con el identificador '{identificador}'.")
            return

        print("Interconexión encontrada.")
        print("1) Modificar interconexión")
        print("2) Dar de baja interconexión")
        print("0) Regresar")
        opcion = input("Ingrese una opción: ")

        while opcion not in ["0", "1", "2"]:
            print("Opción inválida. Por favor, intente de nuevo.")
            opcion = input("Ingrese una opción: ")

        if opcion == "0":
            return
        elif opcion == "1":
            porcentaje = validar_porcentaje("Ingrese el nuevo porcentaje de la interconexión o ingrese 'cancelar' para volver atrás: ")
            if porcentaje is None or porcentaje.lower() == 'cancelar':
                return None

            interconexion.porcentaje = porcentaje
            print("Interconexión modificada correctamente.")
        elif opcion == "2":
            interconexiones_list.remove(interconexion)
            print("Interconexión dada de baja correctamente.")
    except Exception as e:
        print(f"Error: {str(e)}")

def menu_interconexiones():
    while True:
        print("\nInterconexiones:")
        print("1) Alta")
        print("2) Modificación")
        print("0) Regresar")

        opcion = input("Ingrese una opción: ")

        try:
            if opcion == "1":
                alta_interconexion()
            elif opcion == "2":
                modificar_interconexion()
            elif opcion == "0":
                break
            else:
                print("Opción inválida. Intente de nuevo.")
        except Exception as e:
            print(f"Error: {str(e)}")
            continue