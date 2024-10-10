class Vehiculo:
    def __init__(self, marca,modelo, color, peso,puestos):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.peso = peso
        self.puestos = puestos
        
    def arrancar(self):
        print  ("el vehiculo arranco.")
    
    def frenar(self):
        print  ("el vehiculo freno.")
    
    def girar(self):
        print  ("el vehiculo giro.")
    
    def acelerar(self):
        print  ("el vehiculo acelero.")
    
    def estacionar(self):
        print  ("el vehiculo estaciono .")

class Carro(Vehiculo):
    
    def __init__(self, marca, modelo, color, peso, puestos, velocidad, cilindrada):
        super().__init__(marca, modelo, color, peso, puestos)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
        
        
carro = Carro ("nissan", "Versa","rojo",2,3,250,2)


        