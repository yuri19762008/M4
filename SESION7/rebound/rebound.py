class EdadInvalidaError(Exception):
    pass

def obtener_edad():
    flag = True
    while flag:
        try:
            edad = input("Por favor, ingrese su edad: ")
            edad = int(edad)
            if edad < 0:
                raise EdadInvalidaError("La edad no puede ser negativa.")
            return edad
            flag = False
        except ValueError:
            print("Error: Por favor, ingrese un número entero válido.")
        except EdadInvalidaError as e:
            print(f"Error: {e}")

def es_adulto(edad):
    return edad >= 18

def main():
    edad = obtener_edad()
    if es_adulto(edad):
        print("Es Adulto")
    else:
        print("No es un adulto")

if __name__ == "__main__":
    main()