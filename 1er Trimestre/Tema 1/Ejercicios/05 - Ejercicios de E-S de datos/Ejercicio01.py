# Modifica el ejercicio del 3 en raya para que si se produce una excepción se guarde en un archivo de texto información de dicho error. 
# Es necesario almacenar la fecha, hora y error que se ha generado.
import random
import os
from datetime import datetime

# Declaración de constantes para los colores de las fichas
AMARILLO = '\u001b[33m'
BLANCO = '\u001b[37m'
ROJO = '\u001b[31m'
RESET = '\u001b[0m' 
FILEPATH = 'd:\\Users\\alumnado\\Documents\\Inteligencia Artificial & Big Data\\Programacion de Inteligencia Artificial\\1er Trimestre\\Tema 1\\Ejercicios\\05 - Ejercicios de E-S de datos\\'

# Declaraciónd el tablero de juego
tablero =  [[" " for count in range(3)] for count in range(3)]
colores_activos = True

def leer_entero(minimo:int, maximo:int, mensaje:str)->int:
    """ 
        Función para pedir al usuario un numero entre un mínimo y un máximo incluidos mostrando un mensaje 
        minimo: valor mínimo que debe tener valor introducido por el usuario
        maximo: malor máximo que debe tener el valor introducido por el usuario
        mensaje: mensaje a mostrar al usuario para pedirle que introduzca un valor 
    """

    # Iteramos la función hasta que podamos devolver un valor
    while(True):        
        try:
            # Pedimos al usuario que introduzca un valor
            seleccion = int(input(mensaje))

            # Si el valor está entre el mínimo y el máximo devolvemos el valor
            if(minimo <= seleccion and seleccion <= maximo):
                return seleccion
        except ValueError as error:
            # Si tenemos una excepción guardamos el error en un fichero y seguimos iterando el bucle
            f = open(FILEPATH + "Ejercicio01_err.log", "a+")
            f.write(str(datetime.now()) + " --> leer_entero --> " + str(error.args[0]) + "\n")
            f.close

            continue

def cls():
    """ 
        Función que nos permite limpiar el terminal donde se esté ejecutandl el programa 
    """

    os.system('cls' if os.name=='nt' else 'clear')

def pintar_menu():
    """ 
        Función que nos permite mostrar en pantalla el menú del juego 
    """

    print("********************************")
    print("*                              *")
    print("*         TRES EN RAYA         *")
    print("*                              *")
    print("* Seleccione una opción:       *")
    print("* 0 - Salir del juego          *")
    print("* 1 - Jugador Vs. CPU          *")
    print("* 2 - Jugador 1 Vs. Jugador 2  *")
    print("*                              *")
    print("********************************")


def menu_seleccion()->int:
    """ 
        Función para que el usuario vea el menú del juego y seleccione una opción. Esta opción es validada hasta que sea correcta 
        return: un número entero entre 0 y 2 con la opción seleccionada por el usuario
    """

    pintar_menu()
    return leer_entero(0, 2, "Seleccione una opcion entre 0 y 2: ")

def reset_juego():
    """ 
        Función encargada de limpiar la pantalla y reiniciar el tablero 
    """

    cls()
    tablero =  [[" " for count in range(3)] for count in range(3)]

def pintar_color(texto:str, color:type, retorno:bool = False)->str:
    """
        Función que nos permite pintar un texto en el teminar usando código ANSI 
        texto: texto que vamos a mostrar en el terminar
        color: color en el que vamos a pintar el texto
        return: True si queremos añadir un retorno de carro, False en caso contrario
    """

    # Verificamos si tenemos los colores activos en la aplicación y pintamos normalmente o con colores
    # dependiendo de esto
    if(colores_activos):
        if(retorno):
            print(f"{color}" + texto + f"{RESET}")
        else:
            print(f"{color}" + texto + f"{RESET}", end="")
    else:
        if(retorno):
            print(texto)
        else:
            print(texto, end="")

def pintar_tablero():
    """ 
        Función para pintar el tablero en pantalla con el estado actual 
    """

    print("-------------")

    # Iteramos por la filas del tablero
    for x in tablero:
        print("| ", end="") 

        # Iteramos por las oclumnas del tablero
        for y in range(0,3):
            
            if(x[y]) == "X":
                pintar_color("X", AMARILLO)
        
            if(x[y]) == "O":
                pintar_color("O", ROJO)
            
            if(x[y]) == " ":
                print(x[y], end="")

            if(y != 2):
                print(" | ", end="") 
            else:
                print(" |") 

        print("-------------")
    

def mostrar_tablero_info(opcion_menu):
    """ 
        Función para mostrar el tablero y la información relacionada con los jugadores 
        opcion_menu: variable para controlar si el segundo jugador es humano o es la CPU
    """

    # Limpiamos la pantalla
    cls()

    # Mostramos la información de los jugadores
    print("El Jugador 1 juega con ", end="")
    pintar_color("X", AMARILLO, True)
    print("El " + ("Jugador 2" if (opcion_menu == 2) else "Ordenador") + " juega con ", end="")
    pintar_color("O", ROJO, True)
    print("")

    # Pintamos el tablero actual
    pintar_tablero()

def main():
    """ 
        Función principal del juego
    """
    # Reseteamos el juego y mostramos el menú de selección de tipo de partida
    reset_juego()
    opcion = menu_seleccion()    

    # Iteramos siempre y cuando la opción no sea la de salir del juego
    while(opcion > 0):

        # Reseteamos las variables de control para el jugador actual y el ganador
        ganador = -1
        jugador = True

        # Mostramos la información de los jugadores y el tablero actual
        mostrar_tablero_info(opcion)

        # Iteramos mientras no haya un ganador declarado
        while(ganador < 0):

            # Dependiendo de a quien le toque jugar haremos que juege el agente adecuado
            if(jugador):
                colocar_ficha("Jugador 1", "X")
            else:
                if(opcion == 2):
                    colocar_ficha("Jugador 2", "O")
                else:
                    logica_cpu()

            # Modificamos la variable jugador para que en la siguiente ronda juegue el contrario
            jugador = not jugador
            
            # Mostramos el tablero despues de que se haya colocado la ficha
            mostrar_tablero_info(opcion)

            # Buscamos un ganador en esta ronda o un empate porque no queden sitios donde poner fichas
            ganador = comprobar_ganador()
        
        # Mostramos un mensaje dependiendo del resultado de la partida
        if(ganador == 0):
            print("Ha sido un empate!")

        if(ganador == 1):
            print("Ha ganado el Jugador 1!")

        if(ganador == 2):
            print("Ha ganado el " + ("Jugador 2!" if opcion == 2 else "Ordenador!"))

        input("Pulse una tecla para continuar")

        # Reseteamos el juego y volvemos a mostrar el menú de selección de partida
        reset_juego()
        opcion = menu_seleccion()    

    # Si el usuario a decidido acabar de jugar, nos despedimos
    print("Adios!")


def comprobar_fila(fila:int, simbolo:str)->bool:
    """ 
        Función que nos permite comprobar si tenemos tres símbolos iguales en todas las columnas de una fila
        return: True si hay tres simbolos iguales en la fila, False en caso contrario
    """

    for x in range(0,3):
        if(not tablero[fila][x] == simbolo):
            return False
    
    return True

def comprobar_columna(columna:int, simbolo:str)->bool:
    """ 
        Función que nos permite comprobar si tenemos tres símbolos iguales en todas las filas de una columna
        return: True si hay tres simbolos iguales en la columna, False en caso contrario
    """

    for x in range(0,3):
        if(not tablero[x][columna] == simbolo):
            return False
    
    return True


def comprobar_diagonal(simbolo:str)->bool:
    """ 
        Función que nos permite comprobar si tenemos tres símbolos iguales en algunas de las diagonales del tablero de juego
        return: True si hay alguna diagonal que tenga tres simbolos iguales
    """

    if(tablero[0][0] == simbolo and tablero[1][1] == simbolo and tablero[2][2] == simbolo):
        return 1
    elif(tablero[0][2] == simbolo and tablero[1][1] == simbolo and tablero[2][0] == simbolo):
         return 1
    else:
        return 0
        
def comprobar_ganador()->int:
    """ 
        Función que nos permite comprobar si hay algún ganador 
        return: -1 si no hay ganador, 0 si hay un empate, 1 Si el ganador es el jugador 1, 2 si el ganador es el jugador 2
    """

    # Comprobamos si ha ganado el jugador 1
    for x in range(0,3):
        if (comprobar_fila(x, "X")):
            return 1
        if (comprobar_columna(x, "X")):
            return 1
    
    if(comprobar_diagonal("X")):
        return 1

    # Comprobamos si ha ganado el jugador 2
    for x in range(0,3):
        if (comprobar_fila(x, "O")):
            return 2
        if (comprobar_columna(x, "O")):
            return 2
    
    if(comprobar_diagonal("O")):
        return 2

    # Comprobamos si quedan espacios libres para poner fichas, si no es así, es un empate
    if(not any(" " in sub for sub in tablero)):
        return 0

    # Si quedan espacio para poner fichas y aún no ha ganado nadie continuamos
    return -1

def comprobar_celda(fila:int, columna:int, simbolo:str, mostrar_mensaje:bool)->bool:
    """
        Función que nos permite insertar una ficha en una celda siempre que no se encuentre vacía
        fila: fila donde se quiere introducir la ficha
        columna: columna donde se quiere introducir la ficha
        simbolo: tipo de ficher que se va a meter, puede ser X o O
        mostrar_mensaje: mensaje a mostrar en caso de que se quiera introducir una ficha en una posición ocupada
        return: True si se ha conseguido introducir la ficha, False en caso contrario
    """

    if(tablero[fila][columna] == " "):
        tablero[fila][columna] = simbolo
        return True
    else:
        print(mostrar_mensaje)
        return False

def colocar_ficha(nombre_jugador:str, ficha:str):
    """ 
        Función que para que un jugador pueda introducir una ficha
        nombre_jugador: Nombre del jugador que está realizando el movimiento
        ficha: valor de la ficha que se está colocando. Puede ser X o O
    """

    # Si el jugador no es la CPU pedimos que introduzca la fila y la columna donde introducir la ficha
    if(not nombre_jugador == "Ordenador"):
        fila = leer_entero(0, 2, nombre_jugador + " -> Introduzca la fila: ")
        columna = leer_entero(0, 2, nombre_jugador + " -> Introduzca la columna: ")

        # Iteramos mientras que los valores introducidos no sean validos
        while(not comprobar_celda(fila, columna, ficha, "La celda está ocupada, elija de nuevo")):
            fila = leer_entero(0, 2, nombre_jugador + " -> Introduzca la fila: ")
            columna = leer_entero(0, 2, nombre_jugador + " -> Introduzca la columna: ")
    else:
        # Si el jugador es la CPU, hacemos lo mismo, pero seleccionado valores aleatorios para la fila y columna
        fila = random.randint(0, 2)
        columna = random.randint(0, 2)
        while(not comprobar_celda(fila, columna, ficha, "")):
            fila = random.randint(0, 2)
            columna = random.randint(0, 2)

def logica_cpu():
    """
        Función que se encarga de colocar ficha cuadno juega el ordenador
    """
    colocar_ficha("Ordenador", "O")

if __name__ == "__main__":
    main()
