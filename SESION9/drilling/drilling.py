def reemplazar_informacion():
    try:
        # Abrimos el archivo en modo de lectura
        with open("informacion.dat", "r") as archivo:
            contenido = archivo.read()  # Leemos todo el contenido del archivo

        # Contamos cuántas veces aparece la palabra "Información"
        contador = contenido.count("informacion")

        # Reemplazamos "Información" por "Procesamiento"
        nuevo_contenido = contenido.replace("informacion", "Procesamiento")

        # Escribimos el nuevo contenido al archivo
        with open("informacion.dat", "w") as archivo:
            archivo.write(nuevo_contenido)

        # Mostramos cuántos reemplazos se realizaron
        print(f"Se realizaron: {contador} reemplazos")
        print("El contenido del archivo informacion.dat es:")
        print(nuevo_contenido)

    except FileNotFoundError:
        print("El archivo 'informacion.dat' no existe. Asegúrate de que esté en la misma carpeta del script.")

# Ejecutamos la función
reemplazar_informacion()
