# Crea un juego de el ahorcado.
# El juego deberá leer las palabras disponibles para adivinar de un fichero de texto
import random
import csv

FILEPATH = 'd:\\Users\\alumnado\\Documents\\Inteligencia Artificial & Big Data\\Programacion de Inteligencia Artificial\\1er Trimestre\\Tema 1\\Ejercicios\\05 - Ejercicios de E-S de datos\\'
NUM_INTENTOS = 6

# Variables para el contador de partidas ganadas y perdidas
ganadas = 3
perdidas = 7

oculta = []
visible = []

# Abrimos el fichero de destino en modo sobreescribir
# fichero = open(FILEPATH + 'palabras.csv', encoding = 'utf-8')

def leer_diccionario()->list[str]:
    with open(FILEPATH + 'palabras.csv', newline='', encoding = 'utf-8') as f:
        reader = csv.reader(f)
        datos = list(reader)
    return datos

def pintar_cabeza(itentos_restantes:int):
    if(itentos_restantes >= 1):
        print(f"{'  ##   @':15}") 
    else:
        print(f"{'  ##':15}") 

def pintar_torso(itentos_restantes:int):

    if(itentos_restantes >= 4):
        print(f'{"  ##  /|"}', end='') 
        print('\\', end='') 
        print("      ")
    
    if(itentos_restantes == 3):
        print(f'{"  ##  /|":15}') 

    if(itentos_restantes == 2):
        print(f'{"  ##  /":15}') 

    if(itentos_restantes == 1):
        print(f'{"  ##":15}') 


def pintar_piernas(itentos_restantes:int):

    if(itentos_restantes == 6):
        print(f'{"  ##  / "}', end='') 
        print('\\', end='') 
        print("      ")

    if(itentos_restantes == 5):
        print(f'{"  ##  / ":15}') 

    if(itentos_restantes <= 4):
        print(f'{"  ##":15}') 

def pintar_marcadores(intentos_restantes:int, ganadas:int, perdidas:int):
    print("################################################")
    print(f"#  Intentos: {intentos_restantes:3}  Ganadas: {ganadas:3} Perdidas: {perdidas:3}   #")
    print("################################################")


def pintar_pantalla(itentos_restantes:int, palabra_visible:list[chr]):

    print(f"{'  #######':15}")
    print(f"{'  ##   |':15}") 
    pintar_cabeza(itentos_restantes)
    pintar_torso(itentos_restantes)
    pintar_piernas(itentos_restantes)
    print(f"{'  ##':15}")
    
    print(f"{' #########':}", end="")
    print(palabra_visible)

    pintar_marcadores(itentos_restantes, ganadas, perdidas)

def seleccionar_palabra(palabras:list[str])->str:
    return palabras[0][random.randrange(len(palabras[0]))].upper()

def main():
    oculta = list(seleccionar_palabra(leer_diccionario()))
    visible =  list(["_" for count in range(len(oculta))])

    pintar_pantalla(NUM_INTENTOS, visible)



if __name__ == "__main__":
    main()
