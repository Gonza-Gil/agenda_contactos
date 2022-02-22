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
    n = CARPETA + nombre.lower() + apellido.lower() + EXTENSION
    with open(n, 'w', encoding="utf-8") as archivo:
        archivo.write('Nombre: ' + nombre + ' ' + apellido + '\n')
        archivo.write('Número: ' + numero + '\n')
        archivo.write('Categoria: ' + categoria + '\n')


def editar_contacto():
    pass


def ver_contacto(file_name):
    with open(file_name, 'r', encoding='utf-8') as archivo:
        for line in archivo:
            print(line, end='')


def buscar_contacto(name):
    aux_list = os.listdir(CARPETA)
    aux_name = name.lower().replace(' ','')
    aux_name += EXTENSION
    if aux_name in aux_list:
        file_name = aux_list[aux_list.index(aux_name)]
        file_name = CARPETA + file_name
        ver_contacto(file_name)


def eliminar_contacto():
    pass
        

def app():
    crear_directorio()
    buscar_contacto('Gonzalo Gil')
    

app()