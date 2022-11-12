# Parte 1.
#  Crea una clase llamada Persona que permita almacenar la información de una persona, concretamente, queremos almacenar: 
#  dni, nombre, apellidos, edad, teléfono, dirección y correo electrónico.
#  La clase debe de permitir acceder y modificar los datos anteriores, los cuales deben de estar encapsulados y evitar valores erróneos como puede ser un valor 
#  negativo para la edad o una letra. Para ello crea los métodos que creas necesarios.
# 
# Parte 2.
# Crea otra archivo llamado Principal.py que almacene el método main y una lista en la que tener un registro de personas. 
# Elabora las funciones que creas necesarias para realizar un pequeño programa de gestión que permita: añadir, eliminar, modificar o mostrar un registro de la lista.

import os

import Utilidades
from IO import IO_Persona
from Persona import Persona


def mostrar_menu(numero_personas:int):
        print("****************************************************")
        print("*                                                  *")
        print("*               REGISTRO DE PERSONAS               *")
        print("*                                                  *")
        print("****************************************************")
        print("*                                                  *")
        print(f"* Nº de personas registradas: {numero_personas}".ljust(51), end="")
        print("*")         
        print("*                                                  *")
        print("* Pulse el botón correspondiente para cada acción  *")
        print("*                                                  *")
        print("* 1) Añadir una persona                            *")
        print("* 2) Eliminar una persona                          *")
        print("* 3) Modificar una persona del registro            *")
        print("* 4) Mostrar todo el registro simplificado         *")
        print("* 0) Salir                                         *")
        print("*                                                  *")
        print("****************************************************")


def añadir_persona():
    p = Persona()

    while(p.dni is None):
        p.dni = input("Introduzca el dni: ")
    
    while(p.nombre is None):
        p.nombre = input("Introduzca el nombre: ")

    while(p.apellidos is None):
        p.apellidos = input("Introduzca los apellidos: ")

    while(p.edad is None):
        p.edad = input("Introduzca la edad: ")

    while(p.direccion is None):
        p.direccion= input("Introduzca la direccion: ")

    while(p.telefono is None):
        p.telefono = input("Introduzca el telefono: ")

    while(p.email is None):
        p.email = input("Introduzca el email: ")
    
    personas.append(p)

def mostrar_registro_simplificado():
    Utilidades.cls()
    for i in range(len(personas)):
        print(f"[{i + 1}] -> " + str(personas[i]))

def eliminar_persona():
    opcion = -1
    while (opcion  != 0):
        mostrar_registro_simplificado()
        print()
        opcion = opcion = Utilidades.pedir_opcion_menu("Seleccione la persona a eliminar. 0 para salir: ", list(range(0, len(personas) + 1)))
        
        if(opcion != 0):
            del personas[opcion - 1]

def main():
    global personas
    Utilidades.cls()

    fichero = IO_Persona(os.path.join(os.getcwd(), "personas.json"))
    personas = fichero.leer_fichero()
    
    opcion = -1

    while(opcion != 0):

        numero_personas = len(personas)
        mostrar_menu(numero_personas)
        opcion = Utilidades.pedir_opcion_menu("Seleccione una opción del menú: ", [1,2,3,4,5,0])
        Utilidades.cls()

        if(opcion == 1):
            añadir_persona()

        if(opcion == 2):
            eliminar_persona()

        if(opcion == 4):
            mostrar_registro_simplificado()
            print()
            input("Pulse una tecla para continuar ")

    fichero.guardar_fichero(personas)







                

            



    print("Gracias!")


    











if __name__ == "__main__":
    main()
