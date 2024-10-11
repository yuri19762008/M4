

def mi_decorador(funcion):
    def envoltorio(*args,**kwargs):
        print("Esto se ejecuta antes de la funcion decorada")
        resultado = funcion(*args,**kwargs)
        print("Esto se ejecuta despues de la funcion")
        return resultado
    return envoltorio

@mi_decorador
def suma(x,y):
    print (x+y)

suma(2,3)

print("_________")






def decorador(funcion):
    def funcion_modificada():
        print("Antes de llamar a la funcion")
        funcion()
        print("Despues de llamar a la funcion")
        funcion()
    return funcion_modificada

# def saludo():
#     print("Hola yuri")
    
# saludo_modificado = decorador(saludo)
# saludo_modificado()

@decorador
def saludo():
    print("Hola yuri como andas")
saludo()
