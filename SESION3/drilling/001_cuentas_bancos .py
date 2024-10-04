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