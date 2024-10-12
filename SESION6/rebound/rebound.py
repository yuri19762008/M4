#---> YURI URZUA <---

# Definición de variables
suma = 3000
contador = 0

# Intento de división con manejo de excepción
try:
    resultado = suma / contador
    print(resultado)
except ZeroDivisionError:
    print('División por cero.')