# Abrimos el archivo en modo append ('a')
with open('informacion.dat', 'a') as archivo:
    # Agregamos las nuevas líneas al archivo
    nuevas_lineas = [
        "Hola Mundo\n",
        "Este en una nueva línea en el archivo\n",
        "agregando la segunda línea del archivo\n",
        "finalizando la línea agregada\n"
    ]
    archivo.writelines(nuevas_lineas)

print("Líneas agregadas exitosamente al archivo informacion.dat")

# Ahora leemos el contenido del archivo para verificar
with open('informacion.dat', 'r') as archivo:
    contenido = archivo.read()
    print("\nContenido actual del archivo:")
    print(contenido)