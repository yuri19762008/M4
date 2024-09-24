# carga.py

from automovil import Automovil

class Carga(Automovil):
    def __init__(self, marca, modelo, numero_de_ruedas, velocidad, cilindraje, peso_de_carga):
        super().__init__(marca, modelo, numero_de_ruedas, velocidad, cilindraje)
        self.peso_de_carga = peso_de_carga

    def __str__(self):
        return super().__str__() + f", Carga: {self.peso_de_carga} Kg"
