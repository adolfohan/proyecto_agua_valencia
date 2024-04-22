from enumEficacia import Eficiencia
from enumCalidad import Calidad

def validar_identificador(elementos, mensaje, debe_existir=False):
    while True:
        try:
            identificador = input(mensaje + " ingrese 'cancelar' para volver atrás: ")
            if identificador == 'cancelar':
                return None
            identificadores_existentes = [elemento.identificador for elemento in elementos]
            if len(identificador) >= 3 and identificador.isalnum() and (identificador in identificadores_existentes) == debe_existir:
                return identificador
            else:
                if debe_existir:
                    print("Identificador inválido. Debe ser alfanumérico, tener al menos 3 caracteres y existir.")
                else:
                    print("Identificador inválido. Debe ser alfanumérico, tener al menos 3 caracteres y ser único.")
        except KeyboardInterrupt:
            print("Operación interrumpida por el usuario.")
        except Exception as e:
            print(f"Error: {str(e)}")

def obtener_cantidad_litros(mensaje, min_value=0, max_value=None):
    while True:
        try:
            entrada = input(mensaje + " ingrese 'cancelar' para salir: ")
            if entrada.lower() == 'cancelar':
                return None
            cantidad = int(entrada)
            if cantidad >= min_value and (max_value is None or cantidad <= max_value):
                return cantidad
            else:
                print(f"La cantidad debe ser un número entero mayor o igual a {min_value}" + (f" y menor o igual a {max_value}" if max_value else ""))
        except KeyboardInterrupt:
            print("Operación interrumpida por el usuario.")
        except ValueError:
            print("Debe ingresar un número entero válido.")
        except Exception as e:
            print(f"Error: {str(e)}")

def obtener_calidad_agua(mensaje):
    while True:
        try:
            calidad = input(mensaje + " ingrese 'cancelar' para salir: ")
            if calidad.lower() == 'cancelar':
                return None
            elif calidad.lower() in ["potable", "alta", "media", "baja", "nopotabilizable"]:
                return Calidad[calidad.upper()]
            else:
                print("Calidad inválida. Debe ser una de las siguientes: Potable, Alta, Media, Baja, NoPotabilizable.")
        except KeyboardInterrupt:
            print("Operación interrumpida por el usuario.")
        except Exception as e:
            print(f"Error: {str(e)}")

def obtener_eficiencia(mensaje):
    while True:
        try:
            eficiencia = input(mensaje + " ingrese 'cancelar' para salir: ")
            if eficiencia.lower() == 'cancelar':
                return None
            elif eficiencia.lower() in ["alta", "media", "baja"]:
                return Eficiencia[eficiencia.upper()]
            else:
                print("Eficiencia inválida. Debe ser una de las siguientes: Alta, Media, Baja.")
        except KeyboardInterrupt:
            print("Operación interrumpida por el usuario.")
        except Exception as e:
            print(f"Error: {str(e)}")

def validar_porcentaje(mensaje):
    while True:
        try:
            porcentaje = int(input(mensaje + " ingrese 'cancelar' para salir: "))
            if porcentaje == 'cancelar':
                return None
            elif 0 < porcentaje <= 100:
                return porcentaje
            else:
                print("El porcentaje debe estar entre 1 y 100.")
        except KeyboardInterrupt:
            print("Operación interrumpida por el usuario.")
        except ValueError:
            print("Debe ingresar un número entero válido.")
        except Exception as e:
            print(f"Error: {str(e)}")

def obtener_cantidad_dias(mensaje):
    while True:
        try:
            cantidad = int(input(mensaje + " ingrese 'cancelar' para salir: "))
            if cantidad == 'cancelar':
                return None
            elif cantidad > 0:
                return cantidad
            else:
                print("La cantidad de días debe ser un número entero mayor que cero.")
        except KeyboardInterrupt:
            print("Operación interrumpida por el usuario.")
        except ValueError:
            print("Debe ingresar un número entero válido.")
        except Exception as e:
            print(f"Error: {str(e)}")

def obtener_nombre_archivo(mensaje):
    while True:
        try:
            return input(mensaje)
        except KeyboardInterrupt:
            print("Operación interrumpida por el usuario.")
        except Exception as e:
            print(f"Error: {str(e)}")