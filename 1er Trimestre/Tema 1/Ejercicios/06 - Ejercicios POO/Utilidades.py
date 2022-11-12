
import os
from datetime import datetime

import Validaciones


def cls():
    """ 
        Función que nos permite limpiar el terminal donde se esté ejecutandl el programa 
    """

    os.system('cls' if os.name=='nt' else 'clear')
    
def pedir_opcion_menu(texto:str, valores_validos:list) -> int:
    
    # Iteramos la función hasta que podamos devolver un valor
    while(True):        
        try:
            # Pedimos al usuario que introduzca un valor
            seleccion = input(texto)

            if(not Validaciones.validar_entero_entre_valores(int(seleccion), valores_validos)):
                raise ValueError("!El valor introducido no es un número del menú¡")

            return int(seleccion)
        except ValueError as error:
            # Si tenemos una excepción guardamos el error en un fichero y seguimos iterando el bucle
            f = open("errores.log", "a+")
            f.write(str(datetime.now()) + " --> pedir_opcion_menu --> " + str(error.args[0]) + "\n")
            f.close

            continue    