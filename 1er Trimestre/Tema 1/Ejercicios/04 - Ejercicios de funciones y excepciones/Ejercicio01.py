# Crea un módulo de Python que contenga todos los ejercicios creados en las sesiones anteriores. Para
# ello, crea una función para cada uno de ellos. Debes de controlar las posibles excepciones que se
#puedan dar

def t1_e1():
    print("¡hola mundo!")

def t1_e2():
    nombre = input("¿Cual es tu nombre? ")
    print("Saludos", nombre)

def t1_e3():
    try:
        numero = input("Introduce un número: ")
        if type(numero) is int:
            print("El número introducido es el", numero)
        else:
            raise(TypeError)
    except TypeError:
        print("Error!. El valor introducido no es un número")

def t1_e4():
    try:
        numero1 = input("Introduzca el primer número entero: ")
        numero2 = input("Introduzca el segundo número entero: ")
        
        if type(numero1) is int and type(numero2) is int:
            resultado = int(numero1) + int(numero2)
            print("La suma de los dos números es:", resultado)
        else:
            raise(TypeError)
    except TypeError:
        print("Error!. El valor introducido no es un número")




