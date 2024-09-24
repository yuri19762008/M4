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
        if valor < 0 or valor > 150:
            raise ValueError("La edad debe estar entre 0 y 150 años")
        self._edad = valor

    @property
    def peso(self):
        return self._peso

    @peso.setter
    def peso(self, valor):
        if not isinstance(valor, (int, float)):
            raise TypeError("El peso debe ser un número")
        if valor <= 0 or valor > 1000:
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

def crear_animal():
    while True:
        try:
            nombre = input("Ingrese el nombre del animal: ")
            raza = input("Ingrese la raza del animal: ")
            edad = int(input("Ingrese la edad del animal (en años): "))
            peso = float(input("Ingrese el peso del animal (en kg): "))
            
            return Animal(nombre, raza, edad, peso)
        except ValueError as e:
            print(f"Error: {e}. Por favor, intente nuevamente.")
        except TypeError as e:
            print(f"Error: {e}. Por favor, intente nuevamente.")

# Animales predefinidos
perro = Animal("Brando", "San Bernardo", 3, 30)
gato = Animal("Roll", "Persa", 4, 3)

animales = [perro, gato]

# Menú principal
while True:
    print("\n--- Menú Principal ---")
    print("1. Ver animales existentes")
    print("2. Agregar nuevo animal")
    print("3. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        for i, animal in enumerate(animales, 1):
            print(f"\nAnimal {i}:")
            print(animal)
            animal.comer()
            animal.caminar()
            animal.dormir()
    elif opcion == "2":
        nuevo_animal = crear_animal()
        animales.append(nuevo_animal)
        print(f"\n¡{nuevo_animal.nombre} ha sido agregado exitosamente!")
    elif opcion == "3":
        print("¡Gracias por usar el programa!")
        break
    else:
        print("Opción no válida. Por favor, intente nuevamente.")