# Agenda de contactos 
# Acciones que se pueden realizar:
# Agregar un contacto, Editar un contacto, Ver todos los contactos, Buscar un contacto y Eliminar un contacto
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
    if not buscar_contacto(nombre + apellido):
        n = CARPETA + nombre.lower() + apellido.lower() + EXTENSION
        with open(n, 'w', encoding="utf-8") as archivo:
            archivo.write('Nombre: ' + nombre + ' ' + apellido + '\n')
            archivo.write('Número: ' + numero + '\n')
            archivo.write('Categoria: ' + categoria + '\n')
    else:
        print("El contacto ya existe")


def editar_contacto():
    name = input("Ingrese el nombre y apellido del contacto que desea editar ")
    file_name = buscar_contacto(name)
    if file_name:
        print(f'Editando el contacto: {name}')
        nombre = input("Ingrese el nombre del contacto: ")
        apellido = input("Ingrese el apellido del contacto: ")
        numero = input("Ingrese el numero de telefono: ")
        categoria = input("Ingrese la categoria del contacto: ")
        with open(file_name, 'w', encoding="utf-8") as archivo:
            archivo.write('Nombre: ' + nombre + ' ' + apellido + '\n')
            archivo.write('Número: ' + numero + '\n')
            archivo.write('Categoria: ' + categoria + '\n')
        n = CARPETA + nombre.lower() + apellido.lower() + EXTENSION
        os.rename(file_name, n)
    else:
        print("El contacto no existe")


def ver_contacto():
    name = input("Ingrese el nombre y apellido del contacto que desea editar ")
    file_name = buscar_contacto(name)
    if file_name:
        with open(file_name, 'r', encoding='utf-8') as archivo:
            for line in archivo:
                print(line, end='')
    else:
        print("El contacto no existe")
        

def ver_contactos():
    for file_name in os.listdir(CARPETA):
        file_name = CARPETA + file_name
        with open(file_name, 'r', encoding='utf-8') as archivo:
            for line in archivo:
                print(line, end='')
        print("------------------------------------------------")


def buscar_contacto(name):
    aux_list = os.listdir(CARPETA)
    aux_name = name.lower().replace(' ','')
    aux_name += EXTENSION
    if aux_name in aux_list:
        file_name = aux_list[aux_list.index(aux_name)]
        file_name = CARPETA + file_name
        return file_name
    return None


def eliminar_contacto():
    name = input("Ingrese el nombre y apellido del contacto que desea editar ")
    file_name = buscar_contacto(name)
    if file_name:
        os.remove(file_name)
    else:
        print("El contacto no existe")
    
def mostrar_menu():
    print("\n")
    print("------------------------------------------------")    
    print("1) Agregar un nuevo contacto")
    print("2) Editar un contacto")
    print("3) Buscar un contacto")
    print("4) Eliminar un contacto")
    print("5) Ver todos los contactos")
    print("6) Salir")    
        

def app():
    print("Bienvenido a su agenda")
    crear_directorio()
    while True:
        mostrar_menu()
        opcion = int(input("¿Qué desea realizar? "))
        print("\n")
        if opcion == 1:
            crear_contacto()
        elif opcion == 2:
            editar_contacto()
        elif opcion == 3:
            ver_contacto()
        elif opcion == 4:
            eliminar_contacto()
        elif opcion == 5:
            ver_contactos()
        elif opcion == 6:
            break
        else:
            print("Opción no valida. Intente otra vez")

app()