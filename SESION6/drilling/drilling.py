#---> YURI URZUA <---

# Definición del diccionario de usuarios
usuarios = {'001': 'Mark', '002': 'Monica', '003': 'Jacob'}

# ID de usuario que queremos buscar
id_usuario = '004'

# Intentamos acceder al valor de la clave
try:
    print(usuarios[id_usuario])
except KeyError:
    print(f'La clave {id_usuario} no está en el diccionario. Añadiendo clave...')
    usuarios[id_usuario] = 'Ninguno'

# Imprimimos el diccionario actualizado
print(usuarios)