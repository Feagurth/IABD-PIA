import re


def ruta_fichero(ruta_fichero:str) -> bool:
    """
        Función que nos permite validar la ruta de un fichero
        ruta_fichero: La ruta del fichero a validar
        Retorna: True si la ruta es válida, False en caso contrario
    """
    ## pattern = "^(?:[\w]\:|\\{2})(\\{2}[a-z_\-\s0-9\.&]+)+$"
    ## return  False if re.search(pattern, ruta_fichero, re.IGNORECASE) is None else True
    ## TODO: Comprobar esto    
    return True

def validar_entero(valor) -> bool:
    """
        Función para validar si un valor es un entero
        valor: El valor a validar
        Retorna: True si es un entero, False en caso contrario
    """
    try:
        val = int(valor)
        return True
    except:
        return False

def validar_entero_entre_valores(valor_a_validar:int, valores_contra_validar:list) -> bool:
    """
        Función para validar si un entero introducido se encuentra en la lista proporcionadda
        valor_a_validar: El entero a validar
        valores_contra_validar: Lista de valores enteros contra los que validar el valor
        Retorna: True si el valor se encuentra en la lista, False en caso contrario
    """
    if(validar_entero(valor_a_validar)):
         return True if valor_a_validar in valores_contra_validar else False
            

def validar_longitud_cadena(cadena:str, longitud:int) -> bool:
    """
        Función que nos permite validar si una cadena es más larga que la longitud proporcionada o si es nula
        cadena: Cadena a verificar
        longitud: Longitud máxima permitida para la cadena
        Retorna: True si la cadena es inferior a la longitud y mayor que 0, False en caso contrario
    """
    return False if (len(cadena) > longitud or len(cadena) == 0) else True

def validar_edad(edad:str) -> bool:
    """
        Funcion que nos permite validar una edad introducida para que no sea negativa
        edad: La edada a validar
        Retorna: True si la edad es válida, False en caso contrario
    """    
    if(validar_entero(edad)):
        if(int(edad) >= 0 ):
            return True

    return False

def validar_email(email:str) -> bool:
    """
        Función que nos permite validar un email. Validamos el mail y un tamaño máximo de 30 caracteres
        email: El email a validar
        Retorna: True si el email es válido, false en caso contrario
    """
    if(len(email) > 30):
        return False

    pattern = "^[\w.-]+@[\w.-]+\.\w+$"
    return  False if re.search(pattern, email) is None else True

def validar_telefono(telefono:str) -> bool:
    """
        Función que nos permite validar números de telefonos de España, así como no soprepasar los 15 caracteres
        telefono: El telefono a validar
        Retorna: True si el telefono es válido, False en caso contrario
    """
    if(len(telefono) > 15): 
        return False

    pattern = "^(\+34|0034|34)?[6789]\d{8}$"
    return  False if re.search(pattern, telefono) is None else True

def validar_dni(dni:str) -> bool:
    """
        Función que nos permite validar un DNI de España
        dni: dni a validar
        Retorna: True si el dni es válido, False en caso contrario
    """
    pattern = "[0-9]{8}[A-Z]"
    dc = "TRWAGMYFPDXBNJZSQVHLCKE"
    invalidos = {"00000000T", "00000001R", "99999999R"}

    return dni not in invalidos \
        and re.match(pattern, dni) is not None \
        and dni[8] == dc[int(dni[0:8]) % 23]
