# automovil.py

from vehiculo import Vehiculo

class Automovil(Vehiculo):
    def __init__(self, marca, modelo, numero_de_ruedas, velocidad, cilindraje):
        super().__init__(marca, modelo, numero_de_ruedas)
        self.velocidad = velocidad
        self.cilindraje = cilindraje

    def __str__(self):
        return super().__str__() + f" {self.velocidad} Km/h, {self.cilindraje} cc"
