# ---> YURI URZUA LEBUY <---

class Persona:
    def __init__(self, nombre, apellidos, sexo, edad, estatura, peso):
        self._nombre = nombre
        self._apellidos = apellidos
        self._sexo = sexo
        self._edad = edad
        self._estatura = estatura
        self._peso = peso

    # Métodos get
    def get_nombre(self):
        return self._nombre

    def get_apellidos(self):
        return self._apellidos

    def get_sexo(self):
        return self._sexo

    def get_edad(self):
        return self._edad

    def get_estatura(self):
        return self._estatura

    def get_peso(self):
        return self._peso

    # Métodos set
    def set_nombre(self, nombre):
        self._nombre = nombre

    def set_apellidos(self, apellidos):
        self._apellidos = apellidos

    def set_sexo(self, sexo):
        self._sexo = sexo

    def set_edad(self, edad):
        self._edad = edad

    def set_estatura(self, estatura):
        self._estatura = estatura

    def set_peso(self, peso):
        self._peso = peso

    def __str__(self):
        return f"Nombre: {self._nombre}, Apellidos: {self._apellidos}, Sexo: {self._sexo}, Edad: {self._edad} años, Estatura: {self._estatura} mts, Peso: {self._peso} Kg"

# Creando instancias de la clase Persona
persona_1 = Persona("Pedro", "Vivas", "Masculino", 20, 1.78, 68)
persona_2 = Persona("Juan", "Camargo", "Masculino", 18, 1.8, 75)

print("Datos originales:")
print("Persona 1:", persona_1)
print("Persona 2:", persona_2)

# Modificando datos
persona_1.set_edad(21)
persona_2.set_apellidos("Santiago")

print("\nDatos actualizados:")
print("Persona 1:", persona_1)
print("Persona 2:", persona_2)