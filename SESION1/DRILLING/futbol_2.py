class Persona:
    def __init__(self,id, nombre, apellidos, edad ):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad
        self.id = id

    def entrenar(self):
        print(f"{self.nombre} está entrenando.")

    def mostrar_datos(self):
        print(f"Nombre: {self.nombre}\nApellido: {self.apellidos}\nEdad: {self.edad}\nID: {self.id}")

class Futbolista(Persona):
    def __init__(self, nombre, apellidos, edad, id, demarcacion, dorsal):
        super().__init__(nombre, apellidos, edad, id)
        self.demarcacion = demarcacion
        self.dorsal = dorsal

    def jugar(self):
        print(f"{self.nombre} juega como {self.demarcacion}.")

    def mostrar_datos(self):
        super().mostrar_datos()
        print(f"Posición: {self.demarcacion}, Dorsal: {self.dorsal}")

class Entrenador(Persona):
    def __init__(self, nombre, apellidos, edad, id, estrategia):
        super().__init__(nombre, apellidos, edad, id)
        
        self.estrategia = estrategia
        

    def planificar_estrategia(self):
        print(f"{self.nombre} está planificando la estrategia {self.estrategia}.")

    def mostrar_datos(self):
        super().mostrar_datos()
        print(f"Estrategia: {self.estrategia}")

class Masajista(Persona):
    def __init__(self, nombre, apellidos, edad, id, especialidad):
        super().__init__(nombre, apellidos, edad, id)
        self.especialidad = especialidad

    def dar_masaje(self):
        print(f"{self.nombre}, especialista en {self.especialidad}, está dando un masaje.")

    def mostrar_datos(self):
        super().mostrar_datos()
        print(f"Especialidad: {self.especialidad}")

# Función principal para ejecutar y mostrar el comportamiento
def main():
    # Creación de instancias
    futbolista = Futbolista("Carlos", "Gurtierrez Lepe", 28, "ID123", "Delantero", 9)
    entrenador = Entrenador("Miguel", "Perez Gonzalez",  50, "ID456", "4-4-2")
    masajista = Masajista("Ana", "Torroja De Maria", 40, "ID789", "Fisioterapia")

    # Mostrar datos y comportamientos en pantalla
    print("\n--- Futbolista ---")
    futbolista.mostrar_datos()
    futbolista.jugar()
    futbolista.entrenar()

    print("\n--- Entrenador ---")
    entrenador.mostrar_datos()
    entrenador.planificar_estrategia()
    entrenador.entrenar()

    print("\n--- Masajista ---")
    masajista.mostrar_datos()
    masajista.dar_masaje()
    masajista.entrenar()

# Llamada a la función principal para mostrar el comportamiento en pantalla
if __name__ == "__main__":
    main()
