# Definición de la clase A
class A:
    def __init__(self):
        print("Pertenezco a la clase A")
    
    def metodo_a(self):
        print("Método heredado de A")

# Definición de la clase B
class B:
    def __init__(self):
        print("Clase B")
    
    def metodo_b(self):
        print("Método heredado de B")

# Nueva clase C con herencia múltiple de B y A
class C(B, A):
    def __init__(self):
        B.__init__(self)
        A.__init__(self)
    
    def metodo_c(self):
        print("Método es de C")

# Crear un objeto de la clase C
objeto_c = C()

# Llamar a los métodos
objeto_c.metodo_a()
objeto_c.metodo_b()
objeto_c.metodo_c()