# main.py
from vehiculos import Vehiculo, Automovil, Particular, Carga, Bicicleta, Motocicleta

if __name__ == "__main__":
    particular = Particular("Ford", "Fiesta", 4, 180, 500, 5)
    carga = Carga("Daft Trucks", "G 38", 10, 120, 1000, 20000)
    bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera")
    motocicleta = Motocicleta("BMW", "F800s", 2, "Deportiva", "2T", "Doble Viga", 21)

    vehiculos = [particular, carga, bicicleta, motocicleta]

    # Imprimir vehículos
    for vehiculo in vehiculos:
        print(vehiculo)

    # Verificar relaciones de 'motocicleta'
    print("\nVerificando relaciones de 'motocicleta':")
    print("Motocicleta es instancia de Vehiculo:", isinstance(motocicleta, Vehiculo))
    print("Motocicleta es instancia de Automovil:", isinstance(motocicleta, Automovil))
    print("Motocicleta es instancia de Particular:", isinstance(motocicleta, Particular))
    print("Motocicleta es instancia de Carga:", isinstance(motocicleta, Carga))
    print("Motocicleta es instancia de Bicicleta:", isinstance(motocicleta, Bicicleta))
    print("Motocicleta es instancia de Motocicleta:", isinstance(motocicleta, Motocicleta))

    # Guardar los datos en un archivo CSV
    particular.guardar_datos_csv("vehiculos.csv", vehiculos)

    # Leer y mostrar los datos desde el archivo CSV
    print("\nLeyendo datos desde CSV:")
    particular.leer_datos_csv("vehiculos.csv")
