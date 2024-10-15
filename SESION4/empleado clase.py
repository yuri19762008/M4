
#ejercicio de guia desarrollado en clases 15-10-2024

# Decorador personalizado para registrar el cálculo del salario
def registrar_calculo(func):
    def wrapper(*args, **kwargs):
        print(f"Calculando salario para {args[0].nombre}...")
        return func(*args, **kwargs)
    return wrapper

class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    # Usamos @property para controlar el acceso y modificación del salario
    @property
    def salario(self):
        return self._salario

    @salario.setter
    def salario(self, valor):
        if valor < 0:
            raise ValueError("El salario no puede ser negativo")
        self._salario = valor

    # Método de instancia para calcular el salario anual
    @registrar_calculo
    def salario_anual(self):
        return self.salario * 12

    # Método estático para validar si un nombre es válido (solo letras)
    @staticmethod
    def nombre_valido(nombre):
        return nombre.isalpha()

    # Método de clase para crear un empleado desde una cadena "nombre-salario"
    @classmethod
    def desde_cadena(cls, cadena):
        nombre, salario = cadena.split('-')
        return cls(nombre, float(salario))

    # Método dunder __repr__ para representar el objeto como cadena
    def __repr__(self):
        return f"Empleado(nombre={self.nombre}, salario={self.salario})"

class Gerente(Empleado):
    def salario_anual(self):
        # Los gerentes tienen un bono del 10% sobre el salario anual
        salario_base = super().salario_anual()
        return salario_base * 1.1

    def __repr__(self):
        return f"Gerente(nombre={self.nombre}, salario={self.salario})"

class EmpleadoRegular(Empleado):
    def __repr__(self):
        return f"EmpleadoRegular(nombre={self.nombre}, salario={self.salario})"

# Ejemplo de uso del sistema
if __name__ == "__main__":
    # Crear instancias de diferentes tipos de empleados
    gerente = Gerente("Ana", 5000)
    empleado_regular = EmpleadoRegular("Pedro", 3000)

    # Calcular el salario anual de cada uno
    print(gerente.salario_anual())         # Salida: Calculando salario... 66000.0
    print(empleado_regular.salario_anual())# Salida: Calculando salario... 36000.0

    # Usar el Método de Clase para Crear un Empleado
    Gerente_desde_cadena = Gerente.desde_cadena("Carlos-4000")
    print(Gerente_desde_cadena)  # Salida: Empleado(nombre=Carlos, salario=4000.0)

    # Validar el Nombre con el Método Estático
    print(Empleado.nombre_valido("Ana"))  # Salida: True
    print(Empleado.nombre_valido("Ana123"))  # Salida: False
