# funciones.py

import csv
import os

def guardar_datos_csv(vehiculos, nombre_archivo='vehiculos.csv'):
    try:
        modo = 'a' if os.path.exists(nombre_archivo) else 'w'
        with open(nombre_archivo, modo, newline='', encoding='utf-8') as archivo:
            writer = csv.writer(archivo)
            for vehiculo in vehiculos:
                writer.writerow([vehiculo.__class__.__name__, vehiculo.__dict__])
        print(f"Datos guardados exitosamente en {nombre_archivo}")
    except PermissionError:
        print(f"Error de permisos al acceder al archivo {nombre_archivo}")
    except Exception as e:
        print(f"Error al guardar datos en CSV: {str(e)}")

def leer_datos_csv(nombre_archivo='vehiculos.csv'):
    try:
        if not os.path.exists(nombre_archivo):
            raise FileNotFoundError(f"El archivo {nombre_archivo} no existe")
        
        categorias = {
            'Particular': [],
            'Carga': [],
            'Bicicleta': [],
            'Motocicleta': []
        }
        
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            reader = csv.reader(archivo)
            for row in reader:
                if len(row) != 2:
                    print(f"Advertencia: Fila incorrecta en el archivo: {row}")
                    continue
                
                clase, datos_str = row
                try:
                    datos = eval(datos_str)
                except:
                    print(f"Advertencia: Datos inválidos en el archivo: {datos_str}")
                    continue
                
                if clase in categorias:
                    categorias[clase].append(datos)
        
        # Mostrar resultados
        for categoria, datos in categorias.items():
            if datos:
                print(f"\nLista de Vehiculos {categoria}")
                for dato in datos:
                    print(dato)
                    
    except FileNotFoundError as e:
        print(f"Error: {str(e)}")
    except PermissionError:
        print(f"Error de permisos al acceder al archivo {nombre_archivo}")
    except Exception as e:
        print(f"Error al leer datos del CSV: {str(e)}")
