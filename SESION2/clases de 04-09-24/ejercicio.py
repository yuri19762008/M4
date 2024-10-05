class Producto:
    def __init__(self,nombre,precio):
        self.nombre = nombre
        self.precio = precio

class Pedido:

    def __init__(self):
        self.productos = []
    
    def agregar_producto(self,producto):
        self.productos.append(producto)
    
    def mostrar_pedido(self):
        print("Detalle del pedido:")
        total = 0
        for producto in self.productos:
            print(f"Producto {producto.nombre}, Precio {producto.precio}")
            total += producto.precio
        print(f"Total = {total}")

class Cliente:

    def __init__(self,nombre):
        self.nombre = nombre
        self.pedidos =[]
    
    def hacer_pedido(self,productos):
        pedido = Pedido()
        for producto in productos:
            pedido.agregar_producto(producto)
        self.pedidos.append(pedido)
        print(f"El pedido de {self.nombre} fue realizado correctamente.")
        pedido.mostrar_pedido()
        
galletas = Producto("Triton",1000)
jugo = Producto("Zuko",500)
Bebida1 = Producto("Bilz",1500)
Bebida2 =Producto("Pap",1500)

print("Bienvenido a aCuenta")
nombre =input("Ingresa tu nombre: ")
Cliente =Cliente(nombre)


Cliente.hacer_pedido([galletas,jugo])

