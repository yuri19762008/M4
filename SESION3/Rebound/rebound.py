class Persona:
    def __init__(self, numero_identificacion, nombre, apellido):
        self.numero_identificacion = numero_identificacion
        self.nombre = nombre
        self.apellido = apellido

    def obtener_datos(self):
        return f"ID: {self.numero_identificacion}, Nombre: {self.nombre}, Apellido: {self.apellido}"

class Estudiante(Persona):
    def __init__(self, numero_identificacion, nombre, apellido, codigo_alumno, matricula):
        super().__init__(numero_identificacion, nombre, apellido)
        self.codigo_alumno = codigo_alumno
        self.matricula = matricula

    def obtener_datos(self):
        datos_persona = super().obtener_datos()
        return f"{datos_persona}, Código de Alumno: {self.codigo_alumno}, Matrícula: {self.matricula}"

# Ejemplo de uso
persona = Persona("12345678", "Juan", "Pérez")
estudiante = Estudiante("12345678", "Juan", "Pérez", "20240001", "Matriculado")

print(persona.obtener_datos())     # Salida: ID: 12345678, Nombre: Juan, Apellido: Pérez
print(estudiante.obtener_datos())  # Salida: ID: 12345678, Nombre: Juan, Apellido: Pérez, Código de Alumno: 20240001, Matrícula: Matriculado
