# Agenda de contactos 
# Acciones que se pueden realizar:
# Agregar un contacto, Editar un contacto, Ver un contacto, Buscar un contacto y Eliminar un contacto
# App del estilo CRUD

import os


def crear_directorio():
    # Si no existe una carpeta donde almacenar contactos, la creo
    if not os.path.exists('contactos/'):
        os.mkdir('contactos/')
        
def crear_contacto():
    pass

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
    
app()