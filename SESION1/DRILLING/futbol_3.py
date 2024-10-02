class SeleccionFutbol:
    def __init__(self, id, nombre, apellidos, edad):
        self.id = id
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad

    def concentrarse(self):
        return f"{self.nombre} {self.apellidos} se está concentrando."

    def viajar(self):
        return f"{self.nombre} {self.apellidos} está viajando."

    def entrenamiento(self):
        return "Método entrenamiento debe ser implementado en las clases hijas."

    def mostrar_datos(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Apellidos: {self.apellidos}, Edad: {self.edad}"

class Futbolista(SeleccionFutbol):
    def __init__(self, id, nombre, apellidos, edad, dorsal, demarcacion):
        super().__init__(id, nombre, apellidos, edad)
        self.dorsal = dorsal
        self.demarcacion = demarcacion

    def jugar_partido(self):
        return f"{self.nombre} {self.apellidos} está jugando un partido."

    def entrenamiento(self):
        return f"{self.nombre} {self.apellidos} está entrenando."

    def mostrar_datos(self):
        return super().mostrar_datos() + f", Dorsal: {self.dorsal}, Demarcación: {self.demarcacion}"

class Entrenador(SeleccionFutbol):
    def __init__(self, id, nombre, apellidos, edad, id_federacion):
        super().__init__(id, nombre, apellidos, edad)
        self.id_federacion = id_federacion

    def dirigir_partido(self):
        return f"{self.nombre} {self.apellidos} está dirigiendo un partido."

    def entrenamiento(self):
        return f"{self.nombre} {self.apellidos} está dirigiendo un entrenamiento."

    def mostrar_datos(self):
        return super().mostrar_datos() + f", ID Federación: {self.id_federacion}"

class Masajista(SeleccionFutbol):
    def __init__(self, id, nombre, apellidos, edad, titulacion, anios_experiencia):
        super().__init__(id, nombre, apellidos, edad)
        self.titulacion = titulacion
        self.anios_experiencia = anios_experiencia

    def dar_masaje(self):
        return f"{self.nombre} {self.apellidos} está dando un masaje."

    def entrenamiento(self):
        return f"{self.nombre} {self.apellidos} está asistiendo en el entrenamiento."

    def mostrar_datos(self):
        return super().mostrar_datos() + f", Titulación: {self.titulacion}, Años de experiencia: {self.anios_experiencia}"

# Ejemplo de uso
futbolista = Futbolista(1, "Lionel", "Messi", 34, 10, "Delantero")
entrenador = Entrenador(2, "Lionel", "Scaloni", 43, "ARG-001")
masajista = Masajista(3, "Juan", "Pérez", 40, "Fisioterapeuta", 15)

integrantes = [futbolista, entrenador, masajista]

for integrante in integrantes:
    print("Datos del integrante:")
    print(f"{integrante.mostrar_datos()}\n")
    print(integrante.concentrarse())
    print(integrante.viajar())
    print(integrante.entrenamiento())
    print("---> <---")