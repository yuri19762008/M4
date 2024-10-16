import os

def manejar_archivo():
    nombre_archivo = "informacion.dat"
    
    # Verificar si el archivo ya existe
    if os.path.exists(nombre_archivo):
        print(f"El archivo '{nombre_archivo}' ya existe.")
    else:
        # Crear el archivo y escribir el contenido
        try:
            with open(nombre_archivo, 'w') as archivo:
                for i in range(1, 6):
                    archivo.write(f"Datos de información en la línea {i}\n")
            print(f"El archivo '{nombre_archivo}' ha sido creado exitosamente.")
        except IOError:
            print(f"Error al crear el archivo '{nombre_archivo}'.")
            return

    # Leer y mostrar el contenido del archivo
    try:
        with open(nombre_archivo, 'r') as archivo:
            print(f"\nContenido del archivo '{nombre_archivo}':")
            print(archivo.read())
    except IOError:
        print(f"Error al leer el archivo '{nombre_archivo}'.")

if __name__ == "__main__":
    manejar_archivo()