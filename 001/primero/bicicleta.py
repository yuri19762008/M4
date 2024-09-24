# bicicleta.py

from vehiculo import Vehiculo

class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, numero_de_ruedas, tipo):
        super().__init__(marca, modelo, numero_de_ruedas)
        self.tipo = tipo

    def __str__(self):
        return super().__str__() + f", Tipo: {self.tipo}"
