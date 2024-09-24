# particular.py

from automovil import Automovil

class Particular(Automovil):
    def __init__(self, marca, modelo, numero_de_ruedas, velocidad, cilindraje, numero_de_puestos):
        super().__init__(marca, modelo, numero_de_ruedas, velocidad, cilindraje)
        self.numero_de_puestos = numero_de_puestos

    def __str__(self):
        return super().__str__() + f", Puestos: {self.numero_de_puestos}"
