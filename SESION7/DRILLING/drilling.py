

class RangoSalarioError(Exception):
    def __init__(self, salario):
        self.salario = salario
        self.mensaje = f"{salario} -> Salario no está definido en el rango (1000 a 2000)"
        super().__init__(self.mensaje)

def verificar_salario(salario):
    if not (1000 <= salario <= 2000):
        raise RangoSalarioError(salario)
    return salario

def main():
    try:
        salario = float(input("Ingrese el salario: "))
        salario_verificado = verificar_salario(salario)
        print(f"El salario {salario_verificado} está en el rango correcto.")
    except ValueError:
        print("Error: Por favor, ingrese un número válido.")
    except RangoSalarioError as e:
        print(f"RangoSalarioError: {e}")

if __name__ == "__main__":
    main()