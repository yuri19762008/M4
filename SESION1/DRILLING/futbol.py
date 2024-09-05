from abc import ABC, abstractmethod

class SeleccionFutbol(ABC):
    def __init__(self, id, nombre, apellidos, edad):
        self.id = id
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad

    def concentrarse(self):
        print(f"{self.nombre} {self.apellidos} se está concentrando.")

    def viajar(self):
        print(f"{self.nombre} {self.apellidos} está viajando.")

    @abstractmethod
    def entrenar(self):
        pass

class Futbolista(SeleccionFutbol):
    def __init__(self, id, nombre, apellidos, edad, dorsal, demarcacion):
        super().__init__(id, nombre, apellidos, edad)
        self.dorsal = dorsal
        self.demarcacion = demarcacion

    def entrenar(self):
        print(f"El futbolista {self.nombre} {self.apellidos} está entrenando.")

    def jugar_partido(self):
        print(f"El futbolista {self.nombre} {self.apellidos} está jugando un partido.")

class Entrenador(SeleccionFutbol):
    def __init__(self, id, nombre, apellidos, edad, id_federacion):
        super().__init__(id, nombre, apellidos, edad)
        self.id_federacion = id_federacion

    def entrenar(self):
        print(f"El entrenador {self.nombre} {self.apellidos} está dirigiendo el entrenamiento.")

    def planificar_entrenamiento(self):
        print(f"El entrenador {self.nombre} {self.apellidos} está planificando el entrenamiento.")

class Masajista(SeleccionFutbol):
    def __init__(self, id, nombre, apellidos, edad, titulacion, anios_experiencia):
        super().__init__(id, nombre, apellidos, edad)
        self.titulacion = titulacion
        self.anios_experiencia = anios_experiencia

    def entrenar(self):
        print(f"El masajista {self.nombre} {self.apellidos} está asistiendo en el entrenamiento.")

    def dar_masaje(self):
        print(f"El masajista {self.nombre} {self.apellidos} está dando un masaje.")

def input_entero(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Por favor, ingrese un número entero válido.")

def input_string(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Este campo no puede estar vacío. Por favor, inténtelo de nuevo.")

def crear_futbolista():
    print("\nIngrese los datos del Futbolista:")
    id = input_entero("ID: ")
    nombre = input_string("Nombre: ")
    apellidos = input_string("Apellidos: ")
    edad = input_entero("Edad: ")
    dorsal = input_entero("Dorsal: ")
    demarcacion = input_string("Demarcación: ")
    return Futbolista(id, nombre, apellidos, edad, dorsal, demarcacion)

def crear_entrenador():
    print("\nIngrese los datos del Entrenador:")
    id = input_entero("ID: ")
    nombre = input_string("Nombre: ")
    apellidos = input_string("Apellidos: ")
    edad = input_entero("Edad: ")
    id_federacion = input_string("ID Federación: ")
    return Entrenador(id, nombre, apellidos, edad, id_federacion)

def crear_masajista():
    print("\nIngrese los datos del Masajista:")
    id = input_entero("ID: ")
    nombre = input_string("Nombre: ")
    apellidos = input_string("Apellidos: ")
    edad = input_entero("Edad: ")
    titulacion = input_string("Titulación: ")
    anios_experiencia = input_entero("Años de experiencia: ")
    return Masajista(id, nombre, apellidos, edad, titulacion, anios_experiencia)

if __name__ == "__main__":
    try:
        futbolista = crear_futbolista()
        entrenador = crear_entrenador()
        masajista = crear_masajista()

        print("\nDemostrando comportamientos:")
        
        futbolista.concentrarse()
        futbolista.entrenar()
        futbolista.jugar_partido()

        entrenador.concentrarse()
        entrenador.entrenar()
        entrenador.planificar_entrenamiento()

        masajista.concentrarse()
        masajista.entrenar()
        masajista.dar_masaje()
    except Exception as e:
        print(f"Se produjo un error inesperado: {e}")