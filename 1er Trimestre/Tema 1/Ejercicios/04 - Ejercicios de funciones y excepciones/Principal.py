from operator import truediv
import os
import Datos_programa

def leer_entero(minimo:int, maximo:int, mensaje:str):
    """ Función para pedir al usuario un numero entre un mínimo y un máximo incluidos mostrando un mensaje """

    while(True):        
        try:
            seleccion = int(input(mensaje))
            if(minimo <= seleccion and seleccion <= maximo):
                return seleccion
        except ValueError:
            continue

def cls():
    """ Función que nos permite limpiar el terminal donde se esté ejecutandl el programa """

    os.system('cls' if os.name=='nt' else 'clear')

def pintar_menu():
    """ Función que nos permite mostrar en pantalla el menú del juego """

    print("**************************************************")
    print("*                                                *")
    print("*               TRES EN RAYA                     *")
    print("*                                                *")
    print("* Seleccione una opción:                         *")
    print("* 0 - Salir del juego                            *")
    print("* 1 - Jugador Vs. CPU                            *")
    print("* 2 - Jugador 1 Vs. Jugador 2                    *")
    print("*                                                *")
    print("**************************************************")


def menu_seleccion()->int:
    """ Función para que el usuario vea el menú del juego y seleccione una opción
    Esta opción es validada hasta que sea correcta """
    pintar_menu()
    return leer_entero(0, 2, "Seleccione una opcion entre 0 y 2: ")


def reset_juego():
    tablero =  [[" " for count in range(3)] for count in range(3)]

def pintar_tablero():
    """ Función para pintar el tablero en pantalla con el estado actual """

    print("*************")
    for x in Datos_programa.tablero:
        print("* " + x[0] + " * " + x[1] + " * " + x[2] + " *")
        print("*************")    

def mostrar_tablero_info(opcion_menu):
    cls()
    print("El Jugador 1 juega con X")
    print("El " + ("Jugador 2" if (opcion_menu == 2) else "Ordenador") + " juega con O")
    pintar_tablero()

def main():

    reset_juego()
    opcion = menu_seleccion()    

    while(opcion > 0):
        ganador = -1
        jugador = True

        mostrar_tablero_info(opcion)

        while(ganador < 0):

            if(jugador):
                colocar_ficha("Jugador 1", "X")
            else:
                colocar_ficha("Jugador 2" if opcion == 1 else "Ordenador", "O")

            jugador = not jugador
            
            mostrar_tablero_info(opcion)

            ganador = comprobar_ganador()
        
        if(ganador == 0):
            print("Ha sido un empate!")

        if(ganador == 1):
            print("Ha ganado el Jugador 1")

        if(ganador == 2):
            print("Ha ganado el " + "Jugador 2" if opcion == 1 else "ordenador")

    print("Adios!")



      
def comprobar_ganador()->int:
    return -1

def comprobar_celda(fila:int, columna:int, simbolo:str, mostrar_mensaje:bool)->bool:
    if(Datos_programa.tablero[fila][columna] == " "):
        Datos_programa.tablero[fila][columna] = simbolo
        return True
    else:
        print(mostrar_mensaje)
        return False

def colocar_ficha(nombre_jugador:str, ficha:str):
    """ Función que para que un jugador pueda introducir una ficha"""

    fila = leer_entero(0, 2, nombre_jugador + " -> Introduzca la fila: ")
    columna = leer_entero(0, 2, nombre_jugador + " -> Introduzca la columna: ")
    while(not comprobar_celda(fila, columna, ficha, "La celda está ocupada, elija de nuevo")):
        fila = leer_entero(0, 2, nombre_jugador + " -> Introduzca la fila: ")
        columna = leer_entero(0, 2, nombre_jugador + " -> Introduzca la columna: ")

def logica_cpu():
    print("pendiente")

if __name__ == "__main__":
 main()
