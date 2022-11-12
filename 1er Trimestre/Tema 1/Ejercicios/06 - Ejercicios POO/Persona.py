from json import JSONEncoder

import Validaciones


class Persona:

    _dni = None
    _nombre = None
    _apellidos = None
    _edad = None
    _direccion = None
    _telefono = None
    _email = None

    def __init__(self) -> None:
        pass

    @property
    def dni(self):
        return self._dni
    
    @dni.setter
    def dni(self, dni):
        if(Validaciones.validar_dni(dni)):
            self._dni = dni
    
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre):
        longitud_maxima = 25
        if(Validaciones.validar_longitud_cadena(nombre, int(longitud_maxima))):
            self._nombre = nombre

    @property
    def apellidos(self):
        return self._apellidos
    
    @apellidos.setter
    def apellidos(self, apellidos):
        longitud_maxima = 50
        if(Validaciones.validar_longitud_cadena(apellidos, int(longitud_maxima))):
            self._apellidos = apellidos        

    @property
    def edad(self):
        return self._edad
    
    @edad.setter
    def edad(self, edad):
        if(Validaciones.validar_edad(edad)):
            self._edad = edad  

    @property
    def telefono(self):
        return self._telefono
    
    @telefono.setter
    def telefono(self, telefono):
        if(Validaciones.validar_telefono(telefono)):
            self._telefono = telefono

    @property
    def direccion(self):
        return self._direccion
    
    @direccion.setter
    def direccion(self, direccion):
        longitud_maxima = 100
        if(Validaciones.validar_longitud_cadena(direccion, int(longitud_maxima))):
            self._direccion = direccion          
    
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, email):
        if(Validaciones.validar_email(email)):
            self._email = email      

    def nombre_completo(self):
        return self.nombre + " " + self.apellidos

    def __str__(self):
        return (self.dni + ": " + self.nombre_completo())


# subclass JSONEncoder
class PersonaJsonEncoder(JSONEncoder):
        def default(self, o):
            return o.__dict__

class PersonaJsonDecoder():
        def default(self, obj):
            p = Persona()
            p.dni = obj['_dni']
            p.nombre = obj['_nombre'] 
            p.apellidos = obj['_apellidos']
            p.edad = obj['_edad']
            p.telefono = obj['_telefono']
            p.direccion = obj['_direccion']
            p.email= obj['_email']

            return p