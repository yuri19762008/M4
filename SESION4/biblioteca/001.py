class Libro:
    def __init__(self, titulo, autor, id):
        self.__titulo = titulo
        self.__autor = autor
        self.__id = id
        self.__disponible = True

    def get_titulo(self):
        return self.__titulo

    def get_autor(self):
        return self.__autor

    def get_id(self):
        return self.__id

    def esta_disponible(self):
        return self.__disponible

    def prestar(self):
        if self.__disponible:
            self.__disponible = False
            return True
        return False

    def devolver(self):
        self.__disponible = True

class Usuario:
    def __init__(self, nombre, id):
        self.__nombre = nombre
        self.__id = id

    def get_nombre(self):
        return self.__nombre

    def get_id(self):
        return self.__id

class Prestamo:
    def __init__(self, usuario, libro, fecha_prestamo):
        self.__usuario = usuario
        self.__libro = libro
        self.__fecha_prestamo = fecha_prestamo

    def get_usuario(self):
        return self.__usuario

    def get_libro(self):
        return self.__libro

    def get_fecha_prestamo(self):
        return self.__fecha_prestamo

class SistemaBiblioteca:
    def __init__(self):
        self.__libros = []
        self.__usuarios = []
        self.__prestamos = []

    def agregar_libro(self, libro):
        self.__libros.append(libro)

    def agregar_usuario(self, usuario):
        self.__usuarios.append(usuario)

    def prestar_libro(self, usuario, libro):
        if libro.esta_disponible():
            prestamo = Prestamo(usuario, libro, "fecha_actual")  # Aquí deberías usar la fecha real
            self.__prestamos.append(prestamo)
            libro.prestar()
            return True
        return False

    def devolver_libro(self, libro):
        for prestamo in self.__prestamos:
            if prestamo.get_libro() == libro:
                self.__prestamos.remove(prestamo)
                libro.devolver()
                return True
        return False