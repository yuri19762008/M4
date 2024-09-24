# vehiculos.py
import csv

class Vehiculo:
    def __init__(self, marca, modelo, numero_de_ruedas):
        self.marca = marca
        self.modelo = modelo
        self.numero_de_ruedas = numero_de_ruedas

    def __str__(self):
        return f"Marca {self.marca}, Modelo {self.modelo}, {self.numero_de_ruedas} ruedas"

    def guardar_datos_csv(self, nombre_archivo, vehiculos):
        try:
            with open(nombre_archivo, "w", newline='') as archivo:
                writer = csv.writer(archivo)
                for vehiculo in vehiculos:
                    datos = (vehiculo.__class__.__name__, vehiculo.__dict__)
                    writer.writerow(datos)
        except Exception as e:
            print(f"Error al guardar en CSV: {e}")

    def leer_datos_csv(self, nombre_archivo):
        try:
            with open(nombre_archivo, "r") as archivo:
                reader = csv.reader(archivo)
                for row in reader:
                    print(row)
        except Exception as e:
            print(f"Error al leer CSV: {e}")

class Automovil(Vehiculo):
    def __init__(self, marca, modelo, numero_de_ruedas, velocidad, cilindraje):
        super().__init__(marca, modelo, numero_de_ruedas)
        self.velocidad = velocidad
        self.cilindraje = cilindraje

    def __str__(self):
        return super().__str__() + f" {self.velocidad} Km/h, {self.cilindraje} cc"

class Particular(Automovil):
    def __init__(self, marca, modelo, numero_de_ruedas, velocidad, cilindraje, numero_de_puestos):
        super().__init__(marca, modelo, numero_de_ruedas, velocidad, cilindraje)
        self.numero_de_puestos = numero_de_puestos

    def __str__(self):
        return super().__str__() + f", Puestos: {self.numero_de_puestos}"

class Carga(Automovil):
    def __init__(self, marca, modelo, numero_de_ruedas, velocidad, cilindraje, peso_de_carga):
        super().__init__(marca, modelo, numero_de_ruedas, velocidad, cilindraje)
        self.peso_de_carga = peso_de_carga

    def __str__(self):
        return super().__str__() + f", Carga: {self.peso_de_carga} Kg"

class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, numero_de_ruedas, tipo):
        super().__init__(marca, modelo, numero_de_ruedas)
        self.tipo = tipo

    def __str__(self):
        return super().__str__() + f", Tipo: {self.tipo}"

class Motocicleta(Bicicleta):
    def __init__(self, marca, modelo, numero_de_ruedas, tipo, motor, cuadro, nro_radios):
        super().__init__(marca, modelo, numero_de_ruedas, tipo)
        self.motor = motor
        self.cuadro = cuadro
        self.nro_radios = nro_radios

    def __str__(self):
        return super().__str__() + f", Motor: {self.motor}, Cuadro: {self.cuadro}, Nro Radios: {self.nro_radios}"
