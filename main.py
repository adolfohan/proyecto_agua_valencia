from fuentes import menu_fuentes
from plantas import menu_plantas
from centros import menu_centros
from interconexiones import menu_interconexiones
from simulacion import simular_dias
from sistema import mostrar_info_sistema
from ficheros import cargar_datos, guardar_datos

def menu_principal():
    while True:
        print("\nMenú principal:")
        print("1) Fuente hídrica")
        print("2) Planta potabilizadora")
        print("3) Centro de distribución")
        print("4) Interconexión")
        print("5) Días")
        print("6) Info sistema")
        print("7) Ficheros")
        print("0) Salir")

        try:
            opcion = input("Ingrese una opción: ")

            if opcion not in ["1", "2", "3", "4", "5", "6", "7", "0"]:
                raise ValueError("Opción inválida. Intente de nuevo.")

            if opcion == "1":
                menu_fuentes()
            elif opcion == "2":
                menu_plantas()
            elif opcion == "3":
                menu_centros()
            elif opcion == "4":
                menu_interconexiones()
            elif opcion == "5":
                simular_dias()
            elif opcion == "6":
                mostrar_info_sistema()
            elif opcion == "7":
                submenu_ficheros()
            elif opcion == "0":
                break
        except Exception as e:
            print(f"Ha ocurrido un error: {e}")

def submenu_ficheros():
    while True:
        print("Submenú Ficheros:")
        print("1) Cargar datos")
        print("2) Guardar datos")
        print("0) Regresar")

        try:
            opcion = input("Ingrese una opción: ")

            if opcion not in ["1", "2", "0"]:
                raise ValueError("Opción inválida. Intente de nuevo.")

            if opcion == "1":
                cargar_datos()
            elif opcion == "2":
                guardar_datos()
            elif opcion == "0":
                break
        except Exception as e:
            print(f"Ha ocurrido un error: {e}")

if __name__ == "__main__":
    menu_principal()