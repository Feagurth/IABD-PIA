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
import Validaciones
from IO_Persona import IO_Persona
from Persona import Persona


def main()->None:
    """
        Función principal
    """
    
    # Declaramos la variable personas que contendrá una lista de objetos Persona
    global personas

    # Limiamos la terminal
    Utilidades.cls()

    # Creamos un objeto para trabajar con el fichero de personas
    fichero_personas = IO_Persona(os.path.join(os.getcwd(), "personas.json"))

    # Leemos el fichero de personas
    personas = fichero_personas.leer_fichero()
    
    # Inicializamos la opción e iteramos mientras esta no sea 0
    opcion = -1
    while(opcion != 0):

        # Calculamos el tamaño de la lista que tenemos en memoria
        numero_personas = len(personas)

        # Mostramos el menú de opciones del usuario y le pedimos que seleccione una opción
        mostrar_menu(numero_personas)
        opcion = Utilidades.seleccionar_opcion_valida("Seleccione una opción del menú: ", range(0, 6))

        # Una vez el usuario haya seleccionado, limpiamos la pantalla y realizamos la 
        # operación que se haya seleccionado
        Utilidades.cls()

        if(opcion == 1):
            añadir_persona()

        if(opcion == 2):
            eliminar_persona()

        if(opcion == 3):
            modificar_persona()

        if(opcion == 4):
            mostrar_registro_simplificado()
            input("Pulse Intro para continuar ")

        if(opcion == 5):
            mostrar_registro_completo()
            input("Pulse Intro para continuar ")

    # Si el usuario elige la opción de salir, guardamos la lista de personas en el fichero
    # y nos despedimos
    fichero_personas.guardar_fichero(personas)
    print("Gracias!")


def mostrar_menu(numero_personas:int)->None:
    """
        Función que nos pemite mostrar el menú de opciones de la aplicación
        numero_personas: El tamaño de la lista de personas en memoria
    """
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
    print("* 5) Mostrar todo el registro detallado            *")
    print("* 0) Salir                                         *")
    print("*                                                  *")
    print("****************************************************")


def añadir_persona()->None:
    """
        Función que nos permite añadir un nueva persona a la aplicación
    """
    # Creamos un objeto persona
    p = Persona()

    # Iteramos pidiendo al usuario que introduzca el DNI
    while(p.dni is None):
        p.dni = input("Introduzca el dni: ")
    
    # Iteramos pidiendo al usuario que introduzca el Nombre
    while(p.nombre is None):
        p.nombre = input("Introduzca el nombre: ")

    # Iteramos pidiendo al usuario que introduzca los apellidos
    while(p.apellidos is None):
        p.apellidos = input("Introduzca los apellidos: ")

    # Iteramos pidiendo al usuario que introduzca la edad
    while(p.edad is None):
        p.edad = input("Introduzca la edad: ")

    # Iteramos pidiendo al usuario que introduzca la dirección
    while(p.direccion is None):
        p.direccion= input("Introduzca la direccion: ")

    # Iteramos pidiendo al usuario que introduzca el telefono
    while(p.telefono is None):
        p.telefono = input("Introduzca el telefono: ")

    # Iteramos pidiendo al usuario que introduzca el email
    while(p.email is None):
        p.email = input("Introduzca el email: ")
    
    # Añadimos el nuevo objeto a la lista de personas
    personas.append(p)

def mostrar_registro_simplificado()->None:
    """
        Función que nos permite mostrar un registro simple de las personas en la aplicación
    """
    # Limpiamos el terminal
    Utilidades.cls()

    # Iteramos por las personas en a lista
    for i in range(len(personas)):
        # Imprimimos la posición, así como su DNI y su nombre completo
        print(f"[{i + 1}] -> " + str(personas[i]))

    print()

def recuperar_longitud_campo(atributo)->int:
    """
        Función para recuperar el ancho de cada campo para el registro detallado
        atributo: El atributo de la clase Persona del que deseamos saber la longitud permitida
        Retorna: Un entero con la longitud máxima permitida
    """
    if(atributo == "DNI"):
        longitud = 12

    if(atributo == "Nombre"):
        longitud = 19

    if(atributo == "Apellidos"):
        longitud = 30
        
    if(atributo == "Edad"):
        longitud = 5

    if(atributo == "Direccion"):
        longitud = 52

    if(atributo == "Telefono"):
        longitud = 15

    if(atributo == "Email"):
        longitud = 32
    
    return longitud  

def mostrar_registro_completo()->None:
    """
        Función para mostrar un registro completo de las personas en la aplicación
    """
    Utilidades.cls()

    # Pintamos una linea horizontal inicial
    pintar_linea_horizontal()

    # Iteramos por todas las personas de la aplicación
    for i in range(len(personas)):

        # Comprobamos si es la primera iteración
        if(i == 0):           
            # Si es así, pintamos la cabecera del informe y otra linea horizontal
            pintar_cabecera_informe_completo()
            pintar_linea_horizontal()
        
        # Pintamos los datos de la persona por el terminal
        pintar_datos_persona(i)

def pintar_datos_persona(indice)->None:
    """
        Función para pintar lo datos de una persona en el registro completo de personas
        indice: El índice de la lista de personas que indica la persona a pintar
    """

    # Pintamos el identificador
    print("| " + str(indice + 1).ljust(2) + " |", end="")

    # Iteramos por las propiedades de la persona a pintar
    for attr, value in personas[indice].__dict__.items():
        # Normalizamos los atributos y recuperamos la longitud
        atributo = normalizar_atributos(attr)                
        longitud = recuperar_longitud_campo(atributo)            

        # Pintamos los datos de la persona
        print(" " + str(value) + " ".ljust(longitud-len(value)) + " |", end="")        
    
    # Hacemo sun retorno de carro y pintamos una linea horizontal
    print()
    pintar_linea_horizontal()

def pintar_linea_horizontal()->None:
    """
        Función que nos permite pintar una linea horizontal para el registro completo de personas
    """
    print("-" * 192)           


def pintar_cabecera_informe_completo():
    """
        Función que nos permite pintar la cabecera para el registro completo de personas
    """    
    # Pintamos el Id
    print("| Id |", end="") 

    # Iteramos por las propiedades de la promera persona de la lista
    for attr, value in personas[0].__dict__.items():
        
        # Normalizamos los atributos y recuperamos la longitud
        atributo = normalizar_atributos(attr)                
        longitud = recuperar_longitud_campo(atributo)

        # Pintamos los nombres de los atributos
        print(" " + atributo + " ".ljust(longitud - len(atributo)) + " |", end="") 
    
    # Pintamos un retorno de carro
    print()

def eliminar_persona()->None:
    """
        Función que nos permite eliminar una persona de la aplicación
    """    
    # Inicializamos la opcion e iteramos hasta que esta sea 0
    opcion = -1
    while (opcion  != 0):
        # Mostramos el registor simplificado de personas
        mostrar_registro_simplificado()

        # Pedimos al usuario que seleccione una de las personas para eliminarla
        opcion = opcion = Utilidades.seleccionar_opcion_valida("Seleccione la persona a eliminar. 0 para salir: ", list(range(0, len(personas) + 1)))
        
        # Si el usuario ha seleccionado una persona se elimina de la lista de personas
        if(opcion != 0):
            del personas[opcion - 1]

def modificar_persona()->None:
    """
        Función que nos permite modificar los datos de una persona en la aplicación
    """

    # Inicializamos la opcion e iteramos hasta que esta sea 0
    opcion = -1
    while (opcion  != 0):
        # Mostramos el registor simplificado de personas
        mostrar_registro_simplificado()

        # Pedimos al usuario que seleccione una de las personas para modificarla
        opcion = opcion = Utilidades.seleccionar_opcion_valida("Seleccione la persona a modificar. 0 para salir: ", list(range(0, len(personas) + 1)))
        
        # Si el usuario ha seleccionado una persona
        if(opcion != 0):
            # La recuperamos de la lista y pasamos a modificarla
            persona = personas[opcion - 1]
            actualizar_datos_persona(persona)

def actualizar_datos_persona(persona:Persona)->None:
    """
        Función para modificar los datos de una persona
        persona: Objeto Persona con la información a modificar
    """
    # Limpiamos el terminal
    Utilidades.cls()

    # Iteramos los atributos del objeto a modifcar
    for attr, valor in persona.__dict__.items():
        
        # Normalizamos los atributos
        atributo = normalizar_atributos(attr)        

        # Realizamos una petición de datos al usuario para modificar el valor de los datos de la persona
        persona.__dict__[attr] = peticion_datos_persona(atributo, valor) 

def normalizar_atributos(attr)->None:
    """
        Función que nos permite normalizar los atributos de un objeto Persona
    """
    # Eliminamos el caracter _
    atributo = attr.replace("_", "", -1)

    # Ponemos la primera letra en mayúscula excepto si es un DNI, que las ponemos todas
    atributo = atributo.upper() if atributo == "dni" else atributo.capitalize()
    return atributo

def peticion_datos_persona(atributo, valor_actual):
    """
        Función que pide al usuario que modifique los datos de una persona
        atributo: Atributo del que se desea modificar el nombre
        valor_actual: Valor actual del atributo        
    """
    peticion = ""
    if(atributo == "DNI"):
        while (not Validaciones.validar_dni(peticion)):
            peticion = input(f"Introducza un valor para {atributo} o pulse Intro para continuar [{valor_actual}]: ") or valor_actual

    if(atributo == "Nombre"):
        while (not Validaciones.validar_longitud_cadena(peticion, 15)):
            peticion = input(f"Introducza un valor para {atributo} o pulse Intro para continuar [{valor_actual}]: ") or valor_actual

    if(atributo == "Apellidos"):
        while (not Validaciones.validar_longitud_cadena(peticion, 30)):
            peticion = input(f"Introducza un valor para {atributo} o pulse Intro para continuar [{valor_actual}]: ") or valor_actual

    if(atributo == "Edad"):
        while (not Validaciones.validar_edad(peticion)):
            peticion = input(f"Introducza un valor para {atributo} o pulse Intro para continuar [{valor_actual}]: ") or valor_actual

    if(atributo == "Direccion"):
        while (not Validaciones.validar_longitud_cadena(peticion, 50)):
            peticion = input(f"Introducza un valor para {atributo} o pulse Intro para continuar [{valor_actual}]: ") or valor_actual

    if(atributo == "Telefono"):
        while (not Validaciones.validar_telefono(peticion)):
            peticion = input(f"Introducza un valor para {atributo} o pulse Intro para continuar [{valor_actual}]: ") or valor_actual

    if(atributo == "Email"):
        while (not Validaciones.validar_email(peticion)):
            peticion = input(f"Introducza un valor para {atributo} o pulse Intro para continuar [{valor_actual}]: ") or valor_actual

    return peticion

if __name__ == "__main__":
    main()
