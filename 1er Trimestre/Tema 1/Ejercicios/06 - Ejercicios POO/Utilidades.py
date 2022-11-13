
import os
from datetime import datetime

import Validaciones


def cls():
    """ 
        Función que nos permite limpiar el terminal donde se esté ejecutandl el programa 
    """
    os.system('cls' if os.name=='nt' else 'clear')
    
def seleccionar_opcion_valida(texto:str, valores_validos:list) -> int:
    """
        Función que pide al usuario que introduzca un valor entre varios valores válidos
        texto: Texto a mostrar al usuario pidiendo que introduzca el valor
        valores_validos: Lista de enteris que contiene los valores válidos
        Retorna: Un entero con el valor válido de la selección
    """
    
    # Iteramos la función hasta que podamos devolver un valor
    while(True):        
        try:
            # Pedimos al usuario que introduzca un valor
            seleccion = input(texto)

            # Validamos si el valor no se encuentra entre los valores válidos
            if(not Validaciones.validar_entero_entre_valores(int(seleccion), valores_validos)):
                # Si es así elevamos un error
                raise ValueError("¡El valor introducido no es un número válido!")

            # Si la selección es correcta, devolvemos el número como un entero
            return int(seleccion)
        except ValueError as error:
            # Si tenemos una excepción guardamos el error en un fichero y seguimos iterando el bucle
            f = open("errores.log", "a+", encoding = 'utf-8')
            f.write(str(datetime.now()) + " --> pedir_opcion_menu --> Seleccion: " + seleccion + " - " + str(error.args[0]) + "\n")
            f.close

            continue    
