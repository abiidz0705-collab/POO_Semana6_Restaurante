from modelos.platillo import Platillo
from modelos.bebida import Bebida
from servicios.restaurante import Restaurante


def mostrar_menu():


    print("\n========================================")
    print("      SISTEMA DE GESTIÓN DE RESTAURANTE")
    print("========================================")
    print("1. Registrar platillo")
    print("2. Registrar bebida")
    print("3. Mostrar productos")
    print("4. Salir")
    print("========================================")


def registrar_platillo(restaurante):

    print("\n=== REGISTRAR PLATILLO ===")

    nombre = input("Nombre: ")
    
    try:
        precio = float(input("Precio: "))
        tiempo_preparacion = int(input("Tiempo de preparación (min): "))

        platillo = Platillo(
            nombre,
            precio,
            True,  # Por defecto disponible al crearse
            tiempo_preparacion
        )

        if precio > 0:
            restaurante.registrar_platillo(platillo)
        else:
            print("Error: El precio debe ser mayor que cero.")

    except ValueError:
        print("\nError: Los valores numéricos deben ser válidos.")


def registrar_bebida(restaurante):

    print("\n=== REGISTRAR BEBIDA ===")

    nombre = input("Nombre: ")

    try:
        precio = float(input("Precio: "))
        mililitros = int(input("Cantidad (ml): "))

        bebida = Bebida(
            nombre,
            precio,
            True,
            mililitros
        )

        if precio > 0:
            restaurante.registrar_bebida(bebida)
        else:
            print("Error: El precio debe ser mayor que cero.")

    except ValueError:
        print("\nError: Los valores numéricos deben ser válidos.")


def main():

    restaurante = Restaurante()

    while True:

        mostrar_menu()

        opcion = input("Seleccione una opción: ")

        if opcion == "1":

            registrar_platillo(restaurante)

        elif opcion == "2":

            registrar_bebida(restaurante)

        elif opcion == "3":

            restaurante.mostrar_productos()

        elif opcion == "4":

            print("\nGracias por utilizar el sistema.")
            break

        else:

            print("\nOpción no válida. Intente nuevamente.")


if __name__ == "__main__":
    main()