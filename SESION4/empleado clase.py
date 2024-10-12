class Empleado():
    def __init__ (self, nombre,salario):
        self.nombre = nombre
        self.__salario =salario
    
    @property
    def salario(self):
        return self.__salario
    @salario.setter
    def salario(self, salario):
        self.__salario = salario
        
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self,nombre):
        self.__nombre = nombre
        
    def SalarioAnual(self):
        return self.__salario*12
    
    @staticmethod
    def Aquilesbaeza(nombreValidacion):
        return nombreValidacion.isalpha()
    
    @classmethod
    def crearEmpleado(cls,nombreEmpleado):
        aux = nombreEmpleado.split(";")
        return cls(aux[0],aux[1])
    
    def __repr__(self):
        return f"{self.__class__.__name__}(nombre='{self.__nombre}', salario={self.__salario})"
    
    
class Gerente(Empleado):
    def SalarioAnual(self):
        salario_base = super().SalarioAnual()
        return salario_base *1.1
    
    def __repr__(self):
        return f"Gerente(nombre = {self.nombre}, salario = {self.salario})"
    
class EmpleadoRegular(Empleado):
    def __repr__(self):
        return f"EmpleadoRegular (nombre = {self.nombre}, salario = {self.salario})"
    




empleado1 = Empleado("Pepe","5pe")
empleado2 = Empleado.crearEmpleado("Diego;1200000")

print(empleado2.nombre)
print(empleado1.salario)
print(empleado2)