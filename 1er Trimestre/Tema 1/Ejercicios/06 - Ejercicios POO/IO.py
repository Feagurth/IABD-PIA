import json

import Validaciones
from Persona import Persona, PersonaJsonDecoder, PersonaJsonEncoder


class IO_Persona:

    def __init__(self, ruta_fichero) -> None:
        # Validar ruta de fichero
        self.ruta_fichero = ruta_fichero
    
    @property
    def ruta_fichero(self):
        return self._ruta_fichero
    
    @ruta_fichero.setter
    def ruta_fichero(self, ruta_fichero):
        if(Validaciones.ruta_fichero(ruta_fichero)):
            self._ruta_fichero = ruta_fichero
        else:
            raise Exception("Ruta de fichero erronea")


    def leer_fichero(self)->list():
        # Abrimos el fichero en modo lectura para recuperar la información que contiene
        with open(self.ruta_fichero, encoding = 'utf-8') as o:
            datos = json.load(o, object_hook = PersonaJsonDecoder().default)
            
        return datos

    def guardar_fichero(self, personas:list)->None:
        # Abrimos el fichero en modo lectura para recuperar la información que contiene
        with open(self.ruta_fichero, "w", encoding = 'utf-8') as o:
            json.dump(personas, o, cls=PersonaJsonEncoder)