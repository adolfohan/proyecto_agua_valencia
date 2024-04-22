from typing import List
from enumCalidad import Calidad
from utils import seleccionar_elemento, validar_identificador, obtener_calidad_agua, obtener_cantidad_litros

class FuenteHidrica:
    def __init__(self, identificador, calidad, cantidad_litros):
        self.identificador = identificador
        if calidad not in Calidad:
            raise ValueError("La calidad proporcionada no es válida.")
        self.calidad = calidad
        self.cantidad_litros = cantidad_litros
        self.capacidad_asignada = 0
    
    def puede_agregar_interconexion(self, porcentaje=None):
        if porcentaje is None:
            return self.capacidad_asignada < self.cantidad_litros
        else:
            return self.capacidad_asignada + (porcentaje / 100.0) * self.cantidad_litros <= self.cantidad_litros

fuentes: List[FuenteHidrica] = []

def alta_fuente():
    while True:
        try:
            identificador = validar_identificador(fuentes, "Ingrese el identificador de la fuente hídrica o")
            if identificador is None:
                return
            calidad = obtener_calidad_agua("Ingrese la calidad del agua o")
            if calidad is None:
                return
            cantidad_litros = obtener_cantidad_litros("Ingrese la cantidad de litros por día o")
            if cantidad_litros is None:
                return

            fuente = FuenteHidrica(identificador, calidad, cantidad_litros)
            fuentes.append(fuente)
            print("Fuente hídrica agregada correctamente.")

            while True:
                otra_fuente = input("¿Desea agregar otra fuente hídrica? (s/n): ")
                if otra_fuente.lower() in ['s', 'n']:
                    break
                else:
                    print("Opción inválida. Por favor, ingrese 's' o 'n'.")

            if otra_fuente.lower() != 's':
                break
        except Exception as e:
            print(f"Ha ocurrido un error: {e}")

def modificar_fuente():
    try:
        print("\nModificar fuente hídrica:")
        print("1) Ingresar identificador de la fuente hídrica a modificar")
        print("2) Listar todas las fuentes hídricas")
        print("0) Regresar")
        opcion = input("Ingrese una opción: ")

        while opcion not in ["0", "1", "2"]:
            print("Opción inválida. Por favor, intente de nuevo.")
            opcion = input("Ingrese una opción: ")

        if opcion == "0":
            return
        elif opcion == "1":
            identificador = validar_identificador(fuentes, "Ingrese el identificador de la fuente hídrica a modificar o", debe_existir=True)
            if identificador is None:
                return
        elif opcion == "2":
            if not fuentes:
                print("No hay fuentes hídricas dadas de alta.")
                return
            fuente = seleccionar_elemento(fuentes, "Seleccione una fuente hídrica:")
            if fuente is None:
                return
            identificador = fuente.identificador
            print(fuente.identificador)
            print("")

        for fuente in fuentes:
            if fuente.identificador == identificador:
                print("1) Cambiar información")
                print("2) Dar de baja")
                print("0) Regresar")
                opcion = input("Ingrese una opción: ")

                while opcion not in ["0", "1", "2"]:
                    print("Opción inválida. Por favor, intente de nuevo.")
                    opcion = input("Ingrese una opción: ")

                if opcion == "0":
                    return
                elif opcion == "1":
                    calidad = obtener_calidad_agua("Ingrese la nueva calidad del agua o")
                    if calidad is None:
                        return
                    cantidad_litros = obtener_cantidad_litros("Ingrese la nueva cantidad de litros por día o")
                    if cantidad_litros is None:
                        return
                    fuente.calidad = calidad
                    fuente.cantidad_litros = cantidad_litros
                    print("Fuente hídrica modificada correctamente.")
                elif opcion == "2":
                    fuentes.remove(fuente)
                    print("Fuente hídrica dada de baja correctamente.")
                break
        else:
            print("No se encontró una fuente hídrica con el identificador ingresado.")
    except Exception as e:
        print(f"Ha ocurrido un error: {e}")

def menu_fuentes():
    while True:
        print("\nFuentes hídricas:")
        print("1) Alta")
        print("2) Modificación")
        print("0) Regresar")

        try:
            opcion = input("Ingrese una opción: ")

            if opcion not in ["1", "2", "0"]:
                raise ValueError("Opción inválida. Intente de nuevo.")

            if opcion == "1":
                alta_fuente()
            elif opcion == "2":
                modificar_fuente()
            elif opcion == "0":
                break
        except Exception as e:
            print(f"Ha ocurrido un error: {e}")