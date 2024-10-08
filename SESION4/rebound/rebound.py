# ---> YURI URZUA LEBUY <---


class Libro:
    pass

# Creando dos instancias de la clase Libro
libro_1 = Libro()
libro_2 = Libro()

# Asignando atributos a libro_1
libro_1.author = 'Dan Brown'
libro_1.title = 'Inferno'

# Asignando atributos a libro_2
libro_2.author = 'Dan Brown'
libro_2.title = 'The Da Vinci Code'
libro_2.year_of_publishment = 2003

# Imprimiendo el valor del atributo __dict__ de libro_1 y libro_2
print(libro_1.__dict__)
print(libro_2.__dict__)