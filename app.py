# Agenda de contactos 
# Acciones que se pueden realizar:
# Agregar un contacto, Editar un contacto, Ver un contacto, Buscar un contacto y Eliminar un contacto
# App del estilo CRUD

import os

CARPETA = "contactos/"
EXTENSION = '.txt'

def crear_directorio():
    # Si no existe una carpeta donde almacenar contactos, la creo
    if not os.path.exists(CARPETA):
        os.mkdir(CARPETA)
        
def crear_contacto():
    nombre = input("Ingrese el nombre del contacto: ")
    apellido = input("Ingrese el apellido del contacto: ")
    numero = input("Ingrese el numero de telefono: ")
    categoria = input("Ingrese la categoria del contacto: ")
    n = CARPETA + nombre + ' ' + apellido + EXTENSION
    with open(n, 'w', encoding="utf-8") as archivo:
        archivo.write('Nombre: ' + nombre + ' ' + apellido + '\n')
        archivo.write('Número: ' + numero + '\n')
        archivo.write('Categoria: ' + categoria + '\n')

def editar_contacto():
    pass

def ver_contacto():
    pass

def buscar_contacto():
    pass

def eliminar_contacto():
    pass
        


def app():
    crear_directorio()
    crear_contacto()
    
app()