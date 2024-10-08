import datetime
from typing import List, Optional

class Libro:
    def __init__(self, titulo: str, autor: str, id: str):
        self.titulo = titulo
        self.autor = autor
        self.id = id
        self.disponible = True

    def prestar(self) -> bool:
        if self.disponible:
            self.disponible = False
            return True
        return False

    def devolver(self) -> None:
        self.disponible = True

class Usuario:
    def __init__(self, nombre: str, id: str):
        self.nombre = nombre
        self.id = id

class Prestamo:
    def __init__(self, usuario: Usuario, libro: Libro, fecha_prestamo: datetime.datetime):
        self.usuario = usuario
        self.libro = libro
        self.fecha_prestamo = fecha_prestamo

class SistemaBiblioteca:
    def __init__(self):
        self.libros: List[Libro] = []
        self.usuarios: List[Usuario] = []
        self.prestamos: List[Prestamo] = []

    def agregar_libro(self, libro: Libro) -> None:
        self.libros.append(libro)

    def agregar_usuario(self, usuario: Usuario) -> None:
        self.usuarios.append(usuario)

    def obtener_usuario_por_id(self, id_usuario: str) -> Optional[Usuario]:
        return next((usuario for usuario in self.usuarios if usuario.id == id_usuario), None)

    def obtener_libro_por_id(self, id_libro: str) -> Optional[Libro]:
        return next((libro for libro in self.libros if libro.id == id_libro), None)

    def prestar_libro(self, usuario: Usuario, libro: Libro) -> bool:
        if libro.disponible:
            prestamo = Prestamo(usuario, libro, datetime.datetime.now())
            self.prestamos.append(prestamo)
            libro.prestar()
            return True
        return False

    def devolver_libro(self, libro: Libro) -> bool:
        for prestamo in self.prestamos:
            if prestamo.libro == libro:
                self.prestamos.remove(prestamo)
                libro.devolver()
                return True
        return False

    def listar_libros_disponibles(self) -> List[Libro]:
        return [libro for libro in self.libros if libro.disponible]

class Menu:
    def __init__(self):
        self.sistema = SistemaBiblioteca()
        self.usuario_actual: Optional[Usuario] = None

    def mostrar_menu_principal(self) -> None:
        opciones = {
            "1": self.ingresar_como_usuario,
            "2": self.registrar_usuario,
            "3": self.salir
        }
        while True:
            print("\n--- Menú Principal ---")
            print("1. Ingresar como usuario")
            print("2. Registrar nuevo usuario")
            print("3. Salir")
            opcion = input("Seleccione una opción: ")
            accion = opciones.get(opcion)
            if accion:
                if accion():
                    break
            else:
                print("Opción no válida. Por favor, intente de nuevo.")

    def ingresar_como_usuario(self) -> bool:
        id_usuario = input("Ingrese su ID de usuario: ")
        usuario = self.sistema.obtener_usuario_por_id(id_usuario)
        if usuario:
            self.usuario_actual = usuario
            self.mostrar_menu_usuario()
        else:
            print("Usuario no encontrado.")
        return False

    def registrar_usuario(self) -> bool:
        nombre = input("Ingrese su nombre: ")
        id_usuario = input("Ingrese un ID de usuario: ")
        nuevo_usuario = Usuario(nombre, id_usuario)
        self.sistema.agregar_usuario(nuevo_usuario)
        print(f"Usuario {nombre} registrado exitosamente con ID {id_usuario}")
        return False

    def salir(self) -> bool:
        print("Gracias por usar el sistema de biblioteca. ¡Hasta luego!")
        return True

    def mostrar_menu_usuario(self) -> None:
        opciones = {
            "1": self.solicitar_prestamo,
            "2": self.devolver_libro,
            "3": self.ver_libros_disponibles,
            "4": lambda: True
        }
        while True:
            print(f"\n--- Menú de Usuario: {self.usuario_actual.nombre} ---")
            print("1. Solicitar préstamo de libro")
            print("2. Devolver libro")
            print("3. Ver libros disponibles")
            print("4. Cerrar sesión")
            opcion = input("Seleccione una opción: ")
            accion = opciones.get(opcion)
            if accion:
                if accion():
                    self.usuario_actual = None
                    break
            else:
                print("Opción no válida. Por favor, intente de nuevo.")

    def solicitar_prestamo(self) -> bool:
        self.ver_libros_disponibles()
        id_libro = input("Ingrese el ID del libro que desea pedir prestado: ")
        libro = self.sistema.obtener_libro_por_id(id_libro)
        if libro:
            if self.sistema.prestar_libro(self.usuario_actual, libro):
                print(f"Libro '{libro.titulo}' prestado exitosamente.")
            else:
                print("El libro no está disponible para préstamo.")
        else:
            print("Libro no encontrado.")
        return False

    def devolver_libro(self) -> bool:
        id_libro = input("Ingrese el ID del libro que desea devolver: ")
        libro = self.sistema.obtener_libro_por_id(id_libro)
        if libro:
            if self.sistema.devolver_libro(libro):
                print(f"Libro '{libro.titulo}' devuelto exitosamente.")
            else:
                print("No se pudo devolver el libro. Asegúrese de que fue prestado a usted.")
        else:
            print("Libro no encontrado.")
        return False

    def ver_libros_disponibles(self) -> bool:
        print("\nLibros disponibles:")
        for libro in self.sistema.listar_libros_disponibles():
            print(f"ID: {libro.id}, Título: {libro.titulo}, Autor: {libro.autor}")
        return False

if __name__ == "__main__":
    menu = Menu()
    
    # Agregar algunos libros de ejemplo
    menu.sistema.agregar_libro(Libro("Cien años de soledad", "Gabriel García Márquez", "001"))
    menu.sistema.agregar_libro(Libro("1984", "George Orwell", "002"))
    menu.sistema.agregar_libro(Libro("Don Quijote de la Mancha", "Miguel de Cervantes", "003"))
    
    menu.mostrar_menu_principal()