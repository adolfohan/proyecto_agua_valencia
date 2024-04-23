from water_source import water_sources_menu
from water_treatment_plant import plants_menu
from distribution_center import centers_menu
from interconnection import interconnection_menu
from simulation import simulate_days
from system import show_system_info
from ficheros import load_data, save_data

def main_menu():
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
            option = input("Ingrese una opción: ")

            if option not in ["1", "2", "3", "4", "5", "6", "7", "0"]:
                raise ValueError("Opción inválida. Intente de nuevo.")

            if option == "1":
                water_sources_menu()
            elif option == "2":
                plants_menu()
            elif option == "3":
                centers_menu()
            elif option == "4":
                interconnection_menu()
            elif option == "5":
                simulate_days()
            elif option == "6":
                show_system_info()
            elif option == "7":
                file_options()
            elif option == "0":
                break
        except Exception as e:
            print(f"Ha ocurrido un error: {e}")

def file_options():
    while True:
        print("\nSubmenú Ficheros:")
        print("1) Cargar datos")
        print("2) Guardar datos")
        print("0) Regresar")

        try:
            option = input("Ingrese una opción: ")

            if option not in ["1", "2", "0"]:
                raise ValueError("Opción inválida. Intente de nuevo.")

            if option == "1":
                load_data()
            elif option == "2":
                save_data()
            elif option == "0":
                break
        except Exception as e:
            print(f"Ha ocurrido un error: {e}")

if __name__ == "__main__":
    main_menu()