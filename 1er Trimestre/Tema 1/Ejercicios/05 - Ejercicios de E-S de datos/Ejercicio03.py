# Crea un juego de el ahorcado.
# El juego deberá leer las palabras disponibles para adivinar de un fichero de texto

# Importación de librerias
import csv
import os
import random
from datetime import datetime

# Declaración de constantes
FILEPATH = ''
NUM_INTENTOS = 6

# Declaración de variables globales
oculta = []
visible = []
seleccionadas = []

def cls():
    """ 
        Función que nos permite limpiar el terminal donde se esté ejecutandl el programa 
    """

    os.system('cls' if os.name=='nt' else 'clear')

def leer_fichero_palabras(nombre_fichero)->list:
    """"
        Función que nos permite leer un fichero csv con las palabras para adivinar en el juego
        nombre_fichero: Nombre del fichero csv donde se encuentran las palabras
        Retorna: Una lista con las palabras leidas del fichero
    """

    with open(FILEPATH + nombre_fichero, newline='', encoding = 'utf-8') as f:
        reader = csv.reader(f)
        datos = list(reader)
    return datos


def pintar_cabeza(intentos_restantes:int):
    """
        Función que se encarga de pintar la cabeza del muñeco dependiendo del número de intentos restantes
        intentos_restantes: Número de intentos restates
    """
    # Si el número de intentos no es cero pintamos cabeza
    if(intentos_restantes != 0):
        print(f"{'  ##   @':15}") 
    else:
        print(f"{'  ##':15}") 

def pintar_torso(itentos_restantes:int):
    """
        Función que se encarga de pintar el torso del muñeco dependiendo del número de intentos restantes
        intentos_restantes: Número de intentos restates
    """

    # Si el número de intentos es igual o mayor a 4 pintamos cuerpo y brazos
    if(itentos_restantes >= 4):
        print(f'{"  ##  /|"}', end='') 
        print('\\', end='') 
        print("      ")
    
    # Si el número de intentos es 3, puntamos cuerpo y un brazo
    if(itentos_restantes == 3):
        print(f'{"  ##  /|":15}') 

    # Si el número de intentos es 2, puntamos solo el cuerpo cuerpo 
    if(itentos_restantes == 2):
        print(f'{"  ##   |":15}') 

    # Si el número de intentos es 1, no pintamos nada
    if(itentos_restantes == 1):
        print(f'{"  ##":15}') 


def pintar_piernas(itentos_restantes:int):
    """
        Función que se encarga de pintar las piernas del muñeco dependiendo del número de intentos restantes
        intentos_restantes: Número de intentos restates
    """    

    # Si el número de intentos es 6, pintamos las dos piernas
    if(itentos_restantes == 6):
        print(f'{"  ##  / "}', end='') 
        print('\\', end='') 
        print("      ")

    # Si el número de intentos es 5, pintamos solo una pierna
    if(itentos_restantes == 5):
        print(f'{"  ##  / ":15}') 

    # Si el número de intentos es menor o igual a 4, no pintamos nada
    if(itentos_restantes <= 4):
        print(f'{"  ##":15}') 

def pintar_base_cadalso():
    """
        Función encargada de pintar la base del cadalso
    """

    print(f"{'  ##':15}")
    print(f"{' ######### ':}", end="")


def pintar_palabra(palabra_oculta:list):
    """
        Función encargada de pintar la palabra que está adivinándose en pantalla
        palabra_oculta: Lista que contiene el estado actual de la palabra a adivinar
    """
    # Pintamos la concatenación de las letras de la lista centradas
    print(' '.join(palabra_oculta).center(30).center(39))


def pintar_marcadores(intentos_restantes:int, partidas_ganadas:int, partidas_perdidas:int):
    """
        Función encargada de pintar el marcados
        intentos_restantes: Intentos restantes para adivinar la palabra
        partidas_ganadas: Número de partidas ganadas
        partidas_perdidas: Número de partidas perdidas
    """

    print("##################################################")
    print(f"#   Intentos: {intentos_restantes:3}  Ganadas: {partidas_ganadas:3} Perdidas: {partidas_perdidas:3}    #")
    print("##################################################")

    
def pintar_superior_cadalso(letras_seleccionadas:list):
    """
        Función encargada de pintar la parte superior del cadalso y las letras que ya han sido elegidas por el jugador
    """
    # Pintamos la parte superior del cadalso y concatenamos las letras seleccionadas para mostrarse centradas en pantalla
    print(f"{'  #######':15}", end="")
    print(' '.join(letras_seleccionadas).center(30))
    print(f"{'  ##   |':15}") 
    

def pintar_pantalla(intentos_restantes:int, palabra_oculta:list, letras_seleccionadas:list, partidas_ganadas:int, partidas_perdidas:int):
    """
        Función encargada de pintar la pantalla de juego
        intentos_restantes: Número de intentos restantes para adivinar la palabra
        palabra_oculta: Lista con las letras adivinadas y huecos por adivinar en la palabra
        letras_seleccionadas: Lista con las letras seleccionadas hasta ahora
        partidas_ganadas: Número de partidas ganadas
        partidas_perdidas: Número de partidas perdidas
    """

    # Limpiamos la pantalla y la repintamos nuevamente
    cls()
    pintar_superior_cadalso(letras_seleccionadas)
    pintar_cabeza(intentos_restantes)
    pintar_torso(intentos_restantes)
    pintar_piernas(intentos_restantes)
    pintar_base_cadalso()
    pintar_palabra(palabra_oculta)
    pintar_marcadores(intentos_restantes, partidas_ganadas, partidas_perdidas)

def seleccionar_palabra_aleatoria(palabras:list)->str:
    """
        Función encargada de seleccionar aleatoriamente una palabra entre una lista de palabras dadas
        palabras: Lista que contiene todas las palabras entre las que elegir
        Retorna: Una palabra
    """
    return palabras[0][random.randrange(len(palabras[0]))].upper()


def pedir_letra()->chr:
    """
        Función encarga de pedir una letra por teclado al usuario
        Retorna: La letra introducida por el usuario
    """
    
    # Iteramos la función hasta que podamos devolver un valor
    while(True):        
        try:
            # Pedimos al usuario que introduzca un valor
            seleccion = str(input("Introduzca una letra: ")).upper()

            if(not str.isalpha(seleccion)):
                raise ValueError("!El valor introducido no es una letra¡")

            return seleccion
        except ValueError as error:
            # Si tenemos una excepción guardamos el error en un fichero y seguimos iterando el bucle
            f = open(FILEPATH + "Ejercicio03_err.log", "a+")
            f.write(str(datetime.now()) + " --> leer_letra --> " + str(error.args[0]) + "\n")
            f.close

            continue

def descubrir_letra(visible:list, oculta:list, letra:chr) -> bool:
    """
        Función encargada de comprobar una letra introducida forma parte de la palabra a buscar
        visible: Lista con los caracteres de la palabra a adivinar
        oculta: Lista que contiene el estado actual de la palabra a adivinar
        letra: Letra a comprobar
        Retorna: True si se ha encontrado la letra, False en caso contrario
    """

    # Inicializamos la variable de control
    encontrada = False

    # Iteramos por toda la lista de letras de la palabra oculta
    for i in range(len(oculta)):
        
        # Si encontramos la letra en alguna posición de la lista oculta actualizamos el valor en la lista visible
        if(oculta[i] == letra):
            visible[i] = letra
            encontrada = True
    
    # Retornamos el valor de la variable de control
    return encontrada

def comprobar_resolucion(visible:list)->bool:
    """
        Función que comprueba si la palabra ha sido encontrada
        visible: Lista con los caracteres de la palabra a adivinar
        Retorna: True si se ha encontrado la palabra, False en caso contrario
    """
    for x in visible:
        if(x == "_"):
            return False
    else:
        return True

def main():
    """
        Función principal
    """

    ## Inicialización de partidas perdidas y ganads
    perdidas = 0
    ganadas = 0

    # Recuperamos las palabras del fichero
    palabras = leer_fichero_palabras("palabras.csv")
        
    # Iteramos
    while(True):

        # Seleccionamos aleatoriamente una palabra y creamos una lista
        palabra_oculta = list(seleccionar_palabra_aleatoria(palabras))

        # Creamos otra lista del mismo tamaño solo con el carácter _
        palabra_visible =  list(["_" for count in range(len(palabra_oculta))])
        
        # Inicializamos el reto de variables para esta partida
        ganador = 0
        intentos = NUM_INTENTOS
        letras_usadas = []

        # Iteramos siempre y cuando la opción no sea la de salir del juego
        while(ganador == 0):
            
            # Pintamos la pantalla y pedimos una letra al usuario
            pintar_pantalla(intentos, palabra_visible, letras_usadas, ganadas, perdidas)
            letra = pedir_letra()

            # Si la letra introdocida no está en la palabra a buscar y no se ha usado antes perdemos un intento
            if(not descubrir_letra(palabra_visible, palabra_oculta, letra) and (letra not in letras_usadas)):
                intentos -= 1
        
            # Si no quedan intentos, perdemos la partida
            if(intentos == 0):
                perdidas += 1
                ganador = -1

            # Si hemos encontrado la palabra ganamos la partida
            if(comprobar_resolucion(palabra_visible)):
                ganadas =   ganadas +1
                ganador = 1

            # Si no hemos ganado ni perdido, añadimos la letra a la lista de letras usadas si no existía anteriormente
            letras_usadas.append(letra) if letra not in letras_usadas else letras_usadas

        # Pintamos la pantalla
        pintar_pantalla(intentos, palabra_oculta, letras_usadas, ganadas, perdidas)
       
        # Mostramos diferentes mensajes dependiendo de si hemos ganado o hemos perdido
        if(ganador > 0):            
            print("Enhorabuena, ha ganado la partida!")
        else:
            print("Lo siento, ha perdido la partida. La palabra a buscar era " + ''.join(palabra_oculta))

        # Preguntamos al usuario si quiere jugar de nuevo
        if(input("Pulse q para salir del juego o cualquier otra tecla para iniciar una nueva partida: ").upper() == "Q"):
            # Si no quiere jugar de nuevo, rompemos el bucle
            print("Gracias por jugar..!")
            break
    

if __name__ == "__main__":
    main()
