# main.py

from vehiculo import Vehiculo, Automovil, Particular, Carga, Bicicleta, Motocicleta
from funciones import guardar_datos_csv, leer_datos_csv

def mostrar_menu():
    print("\n--- Menú de Opciones ---")
    print("1. Crear automóvil particular")
    print("2. Crear vehículo de carga")
    print("3. Crear bicicleta")
    print("4. Crear motocicleta")
    print("5. Guardar datos en CSV")
    print("6. Leer datos del CSV")
    print("7. Salir")

def main():
    vehiculos = []
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            marca = input("Marca: ")
            modelo = input("Modelo: ")
            nro_ruedas = int(input("Número de ruedas: "))
            velocidad = int(input("Velocidad: "))
            cilindrada = int(input("Cilindrada: "))
            nro_puestos = int(input("Número de puestos: "))
            vehiculo = Particular(marca, modelo, nro_ruedas, velocidad, cilindrada, nro_puestos)
            vehiculos.append(vehiculo)
        
        elif opcion == "2":
            marca = input("Marca: ")
            modelo = input("Modelo: ")
            nro_ruedas = int(input("Número de ruedas: "))
            velocidad = int(input("Velocidad: "))
            cilindrada = int(input("Cilindrada: "))
            carga = int(input("Carga en kg: "))
            vehiculo = Carga(marca, modelo, nro_ruedas, velocidad, cilindrada, carga)
            vehiculos.append(vehiculo)
        
        elif opcion == "3":
            marca = input("Marca: ")
            modelo = input("Modelo: ")
            nro_ruedas = int(input("Número de ruedas: "))
            tipo = input("Tipo de bicicleta (Urbana o Carrera): ")
            vehiculo = Bicicleta(marca, modelo, nro_ruedas, tipo)
            vehiculos.append(vehiculo)
        
        elif opcion == "4":
            marca = input("Marca: ")
            modelo = input("Modelo: ")
            nro_ruedas = int(input("Número de ruedas: "))
            tipo = input("Tipo: ")
            motor = input("Tipo de motor (2T o 4T): ")
            cuadro = input("Tipo de cuadro: ")
            nro_radios = int(input("Número de radios: "))
            vehiculo = Motocicleta(marca, modelo, nro_ruedas, tipo, motor, cuadro, nro_radios)
            vehiculos.append(vehiculo)
        
        elif opcion == "5":
            if vehiculos:
                guardar_datos_csv(vehiculos)
            else:
                print("No hay vehículos para guardar.")
        
        elif opcion == "6":
            leer_datos_csv()
        
        elif opcion == "7":
            print("Saliendo del programa.")
            break
        
        else:
            print("Opción no válida, intente nuevamente.")

if __name__ == "__main__":
    main()
