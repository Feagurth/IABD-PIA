from json import JSONEncoder

import Validaciones


class Persona:
    """
        Clase para almacenar y trabajar con los datos básicos de una persona
    """

    _dni = None
    _nombre = None
    _apellidos = None
    _edad = None
    _direccion = None
    _telefono = None
    _email = None

    def __init__(self) -> None:
        """
            Constructor básico
        """
        pass

    @property
    def dni(self)->str:
        """
            Propiedad para recuperar el DNI de la persona
            Retorna: El DNI de la persona
        """        
        return self._dni
    
    @dni.setter
    def dni(self, dni)->None:
        """
            Propiedad para asignar el dni de la persona
            dni: El dni a asignar a la persona
        """        
        # Validamos si el DNI es válido antes de poder asignarlo
        if(Validaciones.validar_dni(dni)):
            self._dni = dni
    
    @property
    def nombre(self)->str:
        """
            Propiedad para recuperar el nombre de la persona
            Retorna: El nombre de la persona
        """
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre)->None:
        """
            Propiedad para asignar el nombre de la persona
            nombre: El nombre a asignar a la persona
        """        
        # Validamos si el nombre es válido antes de poder asignarlo        
        longitud_maxima = 15
        if(Validaciones.validar_longitud_cadena(nombre, int(longitud_maxima))):
            self._nombre = nombre

    @property
    def apellidos(self)->str:
        """
            Propiedad para recuperar los apellidos de la persona
            Retorna: Los apellidos de la persona
        """        
        return self._apellidos
    
    @apellidos.setter
    def apellidos(self, apellidos)->None:
        """
            Propiedad para asignar los apellidos de la persona
            apellidos: Los apellidos a asignar a la persona
        """        
        # Validamos si los apellidos es válido antes de poder asignarlo        
        longitud_maxima = 30
        if(Validaciones.validar_longitud_cadena(apellidos, int(longitud_maxima))):
            self._apellidos = apellidos        

    @property
    def edad(self)->int:
        """
            Propiedad para recuperar la edad de la persona
            Retorna: La edad de la persona
        """        
        return self._edad
    
    @edad.setter
    def edad(self, edad)->None:
        """
            Propiedad para asignar la edad de la persona
            edad: La edad a asignar a la persona
        """        
        # Validamos si la edad es válida antes de poder asignarlo                
        if(Validaciones.validar_edad(edad)):
            self._edad = edad  

    @property
    def direccion(self)->str:
        """
            Propiedad para recuperar la direccion de la persona
            Retorna: La direccion de la persona
        """                
        return self._direccion
    
    @direccion.setter
    def direccion(self, direccion)->None:
        """
            Propiedad para asignar la direccion de la persona
            direccion: La direccion a asignar a la persona
        """        
        # Validamos si la direccion es válida antes de poder asignarlo                        
        longitud_maxima = 50
        if(Validaciones.validar_longitud_cadena(direccion, int(longitud_maxima))):
            self._direccion = direccion          
    
    @property
    def telefono(self)->str:
        """
            Propiedad para recuperar el telefono de la persona
            Retorna: El telefono de la persona
        """                        
        return self._telefono
    
    @telefono.setter
    def telefono(self, telefono)->None:
        """
            Propiedad para asignar el telefono de la persona
            telefono: El telefono a asignar a la persona
        """        
        # Validamos si el telefono es válido antes de poder asignarlo                
        if(Validaciones.validar_telefono(telefono)):
            self._telefono = telefono

    @property
    def email(self)->str:
        """
            Propiedad para recuperar el emailemail de la persona
            Retorna: El email de la persona
        """        
        return self._email
    
    @email.setter
    def email(self, email)->None:
        """
            Propiedad para asignar el email de la persona
            email: El email a asignar a la persona
        """        
        # Validamos si el email es válido antes de poder asignarlo                        
        if(Validaciones.validar_email(email)):
            self._email = email      

    def nombre_completo(self)->str:
        """
            Función para recuperar el nombre completo de una persona
        """
        return self.nombre + " " + self.apellidos

    def __str__(self):
        """
            Sobrecarga de la función __str__ para mostrar el dni y el nombre completo de la persona
            al pasar el objeto a cadena
            Retorna: El DNI de la persona junto a su nombre completo formateado
        """
        return (self.dni + ": " + self.nombre_completo())

# subclass JSONEncoder
class PersonaJsonEncoder(JSONEncoder):
    """
        Clase para serializar la clase Persona en Json
    """
    def default(self, obj)->dict:
        """
            Función por defecto para la serialización
            obj: Objeto que se ba a serializar
            Retorna: Un diccionario con las propiedades del objeto
        """
        return obj.__dict__

class PersonaJsonDecoder():
    """
        Clase para deserializar un texto Json en un objeto Persona
    """
    def default(self, obj):
        """
            Función por defecto encarga de la deserialización
            obj: Objeto que se va a deserializar
            Retorna: Un objeto Persona con la información cargada del texto Json
        """
        p = Persona()
        p.dni = obj['_dni']
        p.nombre = obj['_nombre'] 
        p.apellidos = obj['_apellidos']
        p.edad = obj['_edad']
        p.direccion = obj['_direccion']
        p.telefono = obj['_telefono']
        p.email= obj['_email']

        return p