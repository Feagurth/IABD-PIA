import json

import Validaciones
from Persona import PersonaJsonDecoder, PersonaJsonEncoder


class IO_Persona:
    """
        Clase para la lectura y escritura del fichero de personas
    """

    def __init__(self, ruta_fichero) -> None:
        """
            Constructor de la clase
            ruta_fichero: Ruta del fichero donde se realizarán las lecturas y escrituras
        """
        self.ruta_fichero = ruta_fichero
    
    @property
    def ruta_fichero(self)->str:
        """
            Propiedad para recuperar la ruta del fichero
            Retorna: La ruta del fichero
        """
        return self._ruta_fichero
    
    @ruta_fichero.setter
    def ruta_fichero(self, ruta_fichero)->None:
        """
            Propiedad para asignar la ruta del fichero
            ruta_fichero: La ruta del fichero a asingar
        """
        # Validamos que la ruta sea correcta si no es así, generamos una excepción
        if(Validaciones.ruta_fichero(ruta_fichero)):
            self._ruta_fichero = ruta_fichero
        else:
            raise Exception("Ruta de fichero erronea")


    def leer_fichero(self)->list():
        """
            Función que nos permite leer el fichero de personas
            Retorna: Lista de objetos Persona con la información leida del fichero
        """
        # Abrimos el fichero en modo lectura para recuperar la información que contiene
        with open(self.ruta_fichero, encoding = 'utf-8') as o:
            # Leemos los datos Json del fichero y los una clase decodificadora propia
            datos = json.load(o, object_hook = PersonaJsonDecoder().default)
        
        # Devolvemos los datos
        return datos

    def guardar_fichero(self, personas:list)->None:
        """
            Función que nos permite guardar la información en el fichero de personas
            personas: Lista de objetos Persona la información de las personas
        """
        # Abrimos el fichero en modo lectura para recuperar la información que contiene
        with open(self.ruta_fichero, "w", encoding = 'utf-8') as o:
            # Volcamos la información de la lista serializándola con su clase codificadora propia
            json.dump(personas, o, cls=PersonaJsonEncoder)