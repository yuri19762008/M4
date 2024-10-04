# --> YURI URZUA LEBUY <--
#creacion de clase animal
class Animal:
    def __init__(self, nombre, raza, edad, peso):
        self._nombre = nombre
        self.raza = raza
        self.edad = edad
        self.peso = peso
    
    def __str__(self):
        return f"Nombre: {self._nombre}, Raza: {self.raza}, Edad: {self.edad} años, Peso: {self.peso} kg"

# Creando instancias de la clase Animal
caballo = Animal("Zeus", "Pura sangre", 5, 450)
leon = Animal("Boulder", "Atlas", 10, 130)

# Imprimiendo la información de los animales
print("Información del caballo:")
print(caballo)
print("\nInformación del león:")
print(leon)