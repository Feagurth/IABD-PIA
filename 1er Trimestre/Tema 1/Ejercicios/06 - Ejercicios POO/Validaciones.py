import re


def ruta_fichero(ruta_fichero:str) -> bool:
     ## pattern = "^(?:[\w]\:|\\{2})(\\{2}[a-z_\-\s0-9\.&]+)+$"
     ## return  False if re.search(pattern, ruta_fichero, re.IGNORECASE) is None else True
     ## TODO: Comprobar esto
     return True

def validar_entero(valor) -> bool:
    try:
        val = int(valor)
        return True
    except:
        return False

def validar_entero_entre_valores(valor_a_validar:int, valores_contra_validar:list) -> bool:
    if(validar_entero(valor_a_validar)):
         return True if valor_a_validar in valores_contra_validar else False
            

def validar_longitud_cadena(cadena:str, longitud:int) -> bool:
    return False if len(cadena) > longitud else True

def validar_edad(edad) -> bool:
    if(validar_entero(edad)):
        if(int(edad) >= 0 ):
            return True
    
    return False

def validar_email(email:str) -> bool:
    pattern = "^[\w.-]+@[\w.-]+\.\w+$"
    return  False if re.search(pattern, email) is None else True

def validar_telefono(telefono:str) -> bool:
    pattern = "^(\+34|0034|34)?[6789]\d{8}$"
    return  False if re.search(pattern, telefono) is None else True

def validar_dni(dni:str) -> bool:
    pattern = "[0-9]{8}[A-Z]"
    dc = "TRWAGMYFPDXBNJZSQVHLCKE"
    invalidos = {"00000000T", "00000001R", "99999999R"}

    return dni not in invalidos \
        and re.match(pattern, dni) is not None \
        and dni[8] == dc[int(dni[0:8]) % 23]
