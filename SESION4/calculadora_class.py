from abc import ABC, abstractmethod

class OperacionMatematica(ABC):
    @abstractmethod
    def calcular(self, *args):
        pass

class Suma(OperacionMatematica):
    def calcular(self, *args):
        return sum(args)

class Resta(OperacionMatematica):
    def calcular(self, *args):
        if len(args) < 2:
            raise ValueError("Se necesitan al menos dos números para la resta")
        return args[0] - sum(args[1:])

class Multiplicacion(OperacionMatematica):
    def calcular(self, *args):
        resultado = 1
        for num in args:
            resultado *= num
        return resultado

class Division(OperacionMatematica):
    def calcular(self, *args):
        if len(args) < 2:
            raise ValueError("Se necesitan al menos dos números para la división")
        if 0 in args[1:]:
            raise ValueError("División por cero")
        resultado = args[0]
        for num in args[1:]:
            resultado /= num
        return resultado

class Calculadora:
    def __init__(self):
        self.operaciones = {
            '1': Suma(),
            '2': Resta(),
            '3': Multiplicacion(),
            '4': Division()
        }

    def realizar_operacion(self, opcion, *args):
        if opcion not in self.operaciones:
            raise ValueError("Operación no válida")
        return self.operaciones[opcion].calcular(*args)

class InterfazUsuario:
    def __init__(self):
        self.calculadora = Calculadora()

    def mostrar_menu(self):
        print("\n---- Calculadora ----")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Salir")

    def obtener_numeros(self):
        numeros = []
        while True:
            entrada = input("Ingrese un número (o presione Enter para terminar): ")
            if entrada == "":
                break
            try:
                numeros.append(float(entrada))
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número válido.")
        return numeros

    def ejecutar(self):
        while True:
            self.mostrar_menu()
            opcion = input("Seleccione una operación (1-5): ")
            
            if opcion == '5':
                print("Gracias por usar la calculadora. ¡Hasta luego!")
                break
            
            if opcion in ['1', '2', '3', '4']:
                numeros = self.obtener_numeros()
                
                if len(numeros) < 2:
                    print("Error: Se necesitan al menos dos números para realizar una operación.")
                    continue
                
                try:
                    resultado = self.calculadora.realizar_operacion(opcion, *numeros)
                    print(f"Resultado: {resultado}")
                except ValueError as e:
                    print(f"Error: {str(e)}")
            else:
                print("Opción no válida. Por favor, seleccione una opción del 1 al 5.")

if __name__ == "__main__":
    interfaz = InterfazUsuario()
    interfaz.ejecutar()