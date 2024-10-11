class Circulo:
    
    pi = 3.14
    
    @classmethod
    def calcular_area(cls,radio):
        return cls.pi * (radio**2)

print(Circulo().calcular_area(3))

c1 =Circulo()

print(c1.calcular_area(4))























class Animal:
    def __init__(self, nombre) -> None:
        self.__nombre = nombre
        
    def mover(self):
        print("el animal se movio")


