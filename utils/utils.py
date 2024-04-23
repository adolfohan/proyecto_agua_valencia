from enums.enumEficiency import Eficiency
from enums.enumQuality import Quality

def validate_id(elements, message, must_exist=False):
    while True:
        try:
            id = input(message + " ingrese 'cancelar' para volver atrás: ")
            if id.lower() == 'cancelar':
                return None
            existing_ids = [element.id for element in elements]
            if len(id) >= 3 and id.isalnum():
                if must_exist and id not in existing_ids:
                    print("Identificador inválido. Debe ser alfanumérico, tener al menos 3 caracteres y existir.")
                elif not must_exist and id in existing_ids:
                    print("Identificador ya existente.")
                else:
                    return id
            else:
                print("Identificador inválido. Debe ser alfanumérico y tener al menos 3 caracteres.")
        except KeyboardInterrupt:
            print("Operación interrumpida por el usuario.")
        except Exception as e:
            print(f"Error: {str(e)}")

def get_liters_quantity(message, min_value=0, max_value=None):
    while True:
        try:
            user_input = input(message + " ingrese 'cancelar' para volver atrás: ")
            if user_input.lower() == 'cancelar':
                return None
            quantity = int(user_input)
            if quantity >= min_value and (max_value is None or quantity <= max_value):
                return quantity
            else:
                print(f"La cantidad debe ser un número entero mayor o igual a {min_value}" + (f" y menor o igual a {max_value}" if max_value else ""))
        except KeyboardInterrupt:
            print("Operación interrumpida por el usuario.")
        except ValueError:
            print("Debe ingresar un número entero válido.")
        except Exception as e:
            print(f"Error: {str(e)}")

def get_water_quality(message):
    while True:
        try:
            quality = input(message + " ingrese 'cancelar' para volver atrás: ")
            if quality.lower() == 'cancelar':
                return None
            elif quality.lower() in ["potable", "alta", "media", "baja", "nopotabilizable"]:
                return Quality[quality.upper()]
            else:
                print("Calidad inválida. Debe ser una de las siguientes: Potable, Alta, Media, Baja, NoPotabilizable.")
        except KeyboardInterrupt:
            print("Operación interrumpida por el usuario.")
        except Exception as e:
            print(f"Error: {str(e)}")

def get_efficiency(message):
    while True:
        try:
            efficiency = input(message + " ingrese 'cancelar' para volver atrás: ")
            if efficiency.lower() == 'cancelar':
                return None
            elif efficiency.lower() in ["alta", "media", "baja"]:
                return Eficiency[efficiency.upper()]
            else:
                print("Eficiencia inválida. Debe ser una de las siguientes: Alta, Media, Baja.")
        except KeyboardInterrupt:
            print("Operación interrumpida por el usuario.")
        except Exception as e:
            print(f"Error: {str(e)}")

def validate_percentage(message):
    while True:
        try:
            percentage = input(message + " ingrese 'cancelar' para volver atrás: ")
            if percentage.lower() == 'cancelar':
                return None
            percentage = float(percentage)
            if 0 < percentage <= 100:
                return percentage
            else:
                print("El porcentaje debe estar entre 1 y 100.")
        except KeyboardInterrupt:
            print("Operación interrumpida por el usuario.")
        except ValueError:
            print("Debe ingresar un número entero válido.")
        except Exception as e:
            print(f"Error: {str(e)}")

def get_number_of_days(message):
    while True:
        try:
            quantity = input(message + " ingrese 'cancelar' para volver atrás: ")
            if quantity.lower() == 'cancelar':
                return None
            quantity = int(quantity)
            if quantity > 0:
                return quantity
            else:
                print("La cantidad de días debe ser un número entero mayor que cero.")
        except KeyboardInterrupt:
            print("Operación interrumpida por el usuario.")
        except ValueError:
            print("Debe ingresar un número entero válido.")
        except Exception as e:
            print(f"Error: {str(e)}")

def get_file_name(message):
    while True:
        try:
            return input(message)
        except KeyboardInterrupt:
            print("Operación interrumpida por el usuario.")
        except Exception as e:
            print(f"Error: {str(e)}")
            
def display_options(elements, message):
    print(message)
    for i, element in enumerate(elements, start=1):
        print(f"{i}) {element.id}")

    while True:
        option = input("Ingrese el número correspondiente o 'cancelar' para volver atrás: ")

        if option.lower() == 'cancelar':
            return None

        try:
            index = int(option) - 1
            if 0 <= index < len(elements):
                return elements[index]
            else:
                print("Opción inválida. Intente de nuevo.")
        except ValueError:
            print("Opción inválida. Intente de nuevo.")
    
def get_user_input(message, valid_options, default=None):
    while True:
        user_input = input(message)
        if user_input in valid_options:
            return user_input
        elif user_input == '' and default is not None:
            return default
        else:
            print("Opción inválida. Por favor, intente de nuevo.")

def handle_exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Ha ocurrido un error: {e}")
    return wrapper