# Sistema de Gestión de Empleados - Versión Mejorada

def registrar_calculo(func):
    def wrapper(*args, **kwargs):
        print(f"Calculando salario para {args[0].nombre}...")
        return func(*args, **kwargs)
    return wrapper

class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if not self.nombre_valido(valor):
            raise ValueError("El nombre debe contener solo letras")
        self._nombre = valor

    @property
    def salario(self):
        return self._salario

    @salario.setter
    def salario(self, valor):
        if valor < 0:
            raise ValueError("El salario no puede ser negativo")
        self._salario = valor

    @registrar_calculo
    def salario_anual(self):
        return self.salario * 12

    @staticmethod
    def nombre_valido(nombre):
        return nombre.replace(" ", "").isalpha()

    @classmethod
    def desde_cadena(cls, cadena):
        nombre, salario = cadena.split('-')
        return cls(nombre, float(salario))

    def __repr__(self):
        return f"{self.__class__.__name__}(nombre='{self.nombre}', salario={self.salario})"

class Gerente(Empleado):
    @registrar_calculo
    def salario_anual(self):
        salario_base = super().salario_anual()
        return salario_base * 1.1

class EmpleadoRegular(Empleado):
    pass

# Demostración del uso del sistema
if __name__ == "__main__":
    print("Creación de empleados:")
    gerente = Gerente("Ana García", 5000)
    empleado_regular = EmpleadoRegular("Pedro López", 3000)
    print(gerente)
    print(empleado_regular)

    print("\nCálculo de salarios anuales:")
    print(f"Salario anual de {gerente.nombre}: {gerente.salario_anual()}")
    print(f"Salario anual de {empleado_regular.nombre}: {empleado_regular.salario_anual()}")

    print("\nCreación de empleado desde cadena:")
    empleado_desde_cadena = Empleado.desde_cadena("Carlos Rodríguez-4000")
    print(empleado_desde_cadena)

    print("\nValidación de nombres:")
    print(f"¿Es válido 'Ana García'? {Empleado.nombre_valido('Ana García')}")
    print(f"¿Es válido 'Ana123'? {Empleado.nombre_valido('Ana123')}")

    print("\nSubclases de Empleado:")
    print(Empleado.__subclasses__())

    print("\nPrueba de validaciones:")
    try:
        Empleado("John Doe123", 3000)
    except ValueError as e:
        print(f"Error al crear empleado: {e}")

    try:
        Empleado("John Doe", -1000)
    except ValueError as e:
        print(f"Error al asignar salario: {e}")