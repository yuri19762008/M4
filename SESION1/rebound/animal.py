class Animal:
    def __init__(self, nombre: str, raza: str, edad: int, peso: float):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.peso = peso

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, valor):
        if not isinstance(valor, int):
            raise TypeError("La edad debe ser un número entero")
        if valor < 0 or valor > 150:  # Asumiendo un límite máximo razonable
            raise ValueError("La edad debe estar entre 0 y 150 años")
        self._edad = valor

    @property
    def peso(self):
        return self._peso

    @peso.setter
    def peso(self, valor):
        if not isinstance(valor, (int, float)):
            raise TypeError("El peso debe ser un número")
        if valor <= 0 or valor > 1000:  # Asumiendo un límite máximo razonable
            raise ValueError("El peso debe ser positivo y menor a 1000 kg")
        self._peso = valor

    def comer(self):
        print(f"{self.nombre} está comiendo.")
    
    def caminar(self):
        print(f"{self.nombre} está caminando.")
    
    def dormir(self):
        print(f"{self.nombre} está durmiendo.")

    def __str__(self):
        return f"{self.nombre} es un {self.raza} de {self.edad} años y pesa {self.peso} kg."

# Creando instancia de Perro
perro = Animal("Brando", "San Bernardo", 3, 30)

# Creando instancia de Gato
gato = Animal("Roll", "Persa", 4, 3)

# Demostrando algunas acciones
print("Información del Perro:")
print(perro)
perro.comer()
perro.caminar()
perro.dormir()

print("\nInformación del Gato:")
print(gato)
gato.comer()
gato.caminar()
gato.dormir()

# Pruebas de validación opcional
print("\nPruebas de validación:")
try:
    animal_edad_negativa = Animal("Test1", "Test", -1, 10)
except ValueError as e:
    print(f"Error de edad negativa: {e}")

try:
    animal_edad_excesiva = Animal("Test2", "Test", 200, 10)
except ValueError as e:
    print(f"Error de edad excesiva: {e}")

try:
    animal_edad_no_entera = Animal("Test3", "Test", 3.5, 10)
except TypeError as e:
    print(f"Error de tipo de edad: {e}")

try:
    animal_peso_negativo = Animal("Test4", "Test", 5, -10)
except ValueError as e:
    print(f"Error de peso negativo: {e}")

try:
    animal_peso_excesivo = Animal("Test5", "Test", 5, 1500)
except ValueError as e:
    print(f"Error de peso excesivo: {e}")