class Banco:
    def __init__(self, nombre, codigo, direccion):
        self.nombre = nombre
        self.codigo = codigo
        self.direccion = direccion
        self.cuentas = []
        self.clientes = []

    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)

    def agregar_cuenta(self, cuenta):
        self.cuentas.append(cuenta)

    def realizar_transferencia(self, cuenta_origen, cuenta_destino, monto):
        if cuenta_origen.retirar(monto):
            cuenta_destino.depositar(monto)
            return True
        return False

class Cliente:
    def __init__(self, nombre, direccion, numero_identificacion):
        self.nombre = nombre
        self.direccion = direccion
        self.numero_identificacion = numero_identificacion
        self.cuentas = []

    def agregar_cuenta(self, cuenta):
        self.cuentas.append(cuenta)

class Cuenta:
    def __init__(self, numero, titular, saldo):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo

    def depositar(self, monto):
        self.saldo += monto

    def retirar(self, monto):
        if self.saldo >= monto:
            self.saldo -= monto
            return True
        return False

    def consultar_saldo(self):
        return self.saldo

class CuentaAhorro(Cuenta):
    def __init__(self, numero, titular, saldo):
        super().__init__(numero, titular, saldo)
        self.cantidad_retiros = 0

    def retirar(self, monto):
        if super().retirar(monto):
            self.cantidad_retiros += 1
            return True
        return False

class CuentaCorriente(Cuenta):
    def __init__(self, numero, titular, saldo, limite):
        super().__init__(numero, titular, saldo)
        self.limite = limite

    def retirar(self, monto):
        if self.saldo - monto >= -self.limite:
            self.saldo -= monto
            return True
        return False

    def es_saldo_rojo(self):
        return self.saldo < 0

# Ejemplo de uso
if __name__ == "__main__":
    # Crear un banco
    banco = Banco("Banco Ejemplo", "BE001", "Calle Principal 123")

    # Crear clientes
    cliente1 = Cliente("Juan Pérez", "Av. Libertad 456", "12345678")
    cliente2 = Cliente("María García", "Calle Independencia 789", "87654321")

    # Agregar clientes al banco
    banco.agregar_cliente(cliente1)
    banco.agregar_cliente(cliente2)

    # Crear cuentas
    cuenta_ahorro = CuentaAhorro("AH001", cliente1, 1000)
    cuenta_corriente = CuentaCorriente("CC001", cliente2, 2000, 500)

    # Agregar cuentas a clientes y banco
    cliente1.agregar_cuenta(cuenta_ahorro)
    cliente2.agregar_cuenta(cuenta_corriente)
    banco.agregar_cuenta(cuenta_ahorro)
    banco.agregar_cuenta(cuenta_corriente)

    # Realizar operaciones
    cuenta_ahorro.depositar(500)
    cuenta_corriente.retirar(2300)

    # Realizar transferencia
    banco.realizar_transferencia(cuenta_ahorro, cuenta_corriente, 300)

    # Imprimir información
    print(f"Banco: {banco.nombre}")
    print(f"Clientes: {len(banco.clientes)}")
    print(f"Cuentas: {len(banco.cuentas)}")
    print("\nInformación de cuentas:")
    print(f"Cuenta Ahorro ({cuenta_ahorro.numero}):")
    print(f"  Titular: {cuenta_ahorro.titular.nombre}")
    print(f"  Saldo: ${cuenta_ahorro.consultar_saldo()}")
    print(f"  Cantidad de retiros: {cuenta_ahorro.cantidad_retiros}")
    print(f"\nCuenta Corriente ({cuenta_corriente.numero}):")
    print(f"  Titular: {cuenta_corriente.titular.nombre}")
    print(f"  Saldo: ${cuenta_corriente.consultar_saldo()}")
    print(f"  Saldo en rojo: {'Sí' if cuenta_corriente.es_saldo_rojo() else 'No'}")