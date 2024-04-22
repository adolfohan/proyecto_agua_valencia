from typing import List
from enumEficacia import Eficiencia
from utils import validar_identificador, obtener_eficiencia, obtener_cantidad_litros

class PlantaPotabilizadora:
    def __init__(self, identificador, eficiencia, cantidad_litros_maxima):
        self.identificador = identificador
        if eficiencia not in Eficiencia:
            raise ValueError("La eficiencia proporcionada no es válida.")
        self.eficiencia = eficiencia
        self.cantidad_litros_maxima = cantidad_litros_maxima
        self.capacidad_asignada = 0
        self.agua_recibida = 0
        self.agua_potabilizada = 0
        
    def puede_agregar_interconexion(self, porcentaje=None):
        if porcentaje is None:
            return self.capacidad_asignada < self.cantidad_litros_maxima
        else:
            return self.capacidad_asignada + (porcentaje / 100.0) * self.cantidad_litros_maxima <= self.cantidad_litros_maxima

plantas: List[PlantaPotabilizadora] = []

def alta_planta():
    while True:
        try:
            identificador = validar_identificador(plantas, "Ingrese el identificador de la planta potabilizadora o")
            if identificador is None:
                return
            eficiencia = obtener_eficiencia("Ingrese la eficiencia de la planta o")
            if eficiencia is None:
                return
            cantidad_litros_maxima = obtener_cantidad_litros("Ingrese la cantidad máxima de litros por día o")
            if cantidad_litros_maxima is None:
                return

            planta = PlantaPotabilizadora(identificador, eficiencia, cantidad_litros_maxima)
            plantas.append(planta)
            print("Planta potabilizadora agregada correctamente.")

            while True:
                otra_planta = input("¿Desea agregar otra planta potabilizadora? (s/n): ")
                if otra_planta.lower() in ['s', 'n']:
                    break
                else:
                    print("Opción inválida. Por favor, ingrese 's' o 'n'.")

            if otra_planta.lower() != 's':
                break
        except ValueError as e:
            print(f"Error: {str(e)}")

def modificar_planta():
    try:
        print("\nModificar planta potabilizadora:")
        print("1) Ingresar identificador de la planta potabilizadora a modificar")
        print("2) Listar todas las plantas potabilizadoras")
        print("0) Regresar")
        opcion = input("Ingrese una opción: ")
        
        while opcion not in ["0", "1", "2"]:
            print("Opción inválida. Por favor, intente de nuevo.")
            opcion = input("Ingrese una opción: ")

        if opcion == "0":
            return
        elif opcion == "2":
            if not plantas:
                print("No hay plantas potabilizadoras dadas de alta.")
                return
            for planta in plantas:
                print(planta.identificador)
            print("")
        
        identificador = validar_identificador(plantas, "Ingrese el identificador de la planta potabilizadora a modificar o", debe_existir=True)
        if identificador is None:
            return
        planta_encontrada = None

        for planta in plantas:
            if planta.identificador == identificador:
                planta_encontrada = planta
                break

        if planta_encontrada is not None:
            print("Planta encontrada.")
            print("1) Modificar planta")
            print("2) Dar de baja planta")
            print("0) Regresar")
            opcion = input("Ingrese una opción: ")
        
            while opcion not in ["0", "1", "2"]:
                print("Opción inválida. Por favor, intente de nuevo.")
                opcion = input("Ingrese una opción: ")

            if opcion == "0":
                return
            elif opcion == "1":
                eficiencia = obtener_eficiencia("Ingrese la nueva eficiencia de la planta o")
                if eficiencia is None:
                    return
                cantidad_litros_maxima = obtener_cantidad_litros("Ingrese la nueva cantidad máxima de litros por día o")
                if cantidad_litros_maxima is None:
                    return

                planta_encontrada.eficiencia = eficiencia
                planta_encontrada.cantidad_litros_maxima = cantidad_litros_maxima

                print("Planta potabilizadora modificada correctamente.")
            elif opcion == "2":
                plantas.remove(planta_encontrada)
                print("Planta potabilizadora dada de baja correctamente.")
        else:
            print("Planta no encontrada.")
    except Exception as e:
        print(f"Error: {str(e)}")

def menu_plantas():
    while True:
        print("\nPlantas potabilizadoras:")
        print("1) Alta")
        print("2) Modificación")
        print("0) Regresar")

        opcion = input("Ingrese una opción: ")

        try:
            if opcion == "1":
                alta_planta()
            elif opcion == "2":
                modificar_planta()
            elif opcion == "0":
                break
            else:
                print("Opción inválida. Intente de nuevo.")
        except ValueError as e:
            print(f"Error: {str(e)}")
        except Exception as e:
            print(f"Error inesperado: {str(e)}")