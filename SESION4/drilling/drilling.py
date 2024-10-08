# ---> YURI URZUA <---

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def movimiento(self):
        return "caminando"

class Maratonista(Persona):
    def movimiento(self):
        return "trotando"

class Ciclista(Persona):
    def movimiento(self):
        return "rodando"

# Ejemplo de uso
persona = Persona("Juan")
maratonista = Maratonista("María")
ciclista = Ciclista("Pedro")

print(f"{persona.nombre} está {persona.movimiento()}")
print(f"{maratonista.nombre} está {maratonista.movimiento()}")
print(f"{ciclista.nombre} está {ciclista.movimiento()}")