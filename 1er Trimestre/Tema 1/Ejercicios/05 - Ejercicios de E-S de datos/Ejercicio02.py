# A partir de la información disponible en el archivo JSON que hay en la web datos.gob.es (https://datos.gob.es/es/catalogo/ea0019768-autores-espanoles-en-dominio-publico-en-2020-fallecidos-en-1939) sobre autores literarios, 
# obtener un listado de todas las mujeres que lo componen. Guardar en un archivo CSV el id_BNE, nombre y género de los autores que nacieron en 1865.
import csv
import json

FILEPATH = ''

# Abrimos el fichero en modo lectura para recuperar la información que contiene
with open(FILEPATH + 'dominiopublico1939.json', encoding = 'utf-8') as o:
    datos = json.load(o)

# Definimos una lista para almacenar los autores que nacieronen 1865
autores = []

# Abrimos el fichero de destino en modo sobreescribir
s = open(FILEPATH + 'Ejercicio02_out.csv', "w", newline='', encoding = 'utf-8')

print("Listado de mujeres")
print("------------------")

# Iteramos por los datos almacenados en el fichero json
for d in datos:

    # Comprobamos si el registro tiene la clave género y si su valor es distinto de MASCULINO    
    if("género" in d):
        if((d["género"].upper()) != "MASCULINO"):
            # Si es así, imprimimos el nombre por pantalla
            print(d["nombre_de_persona"])
    
    # Comprobamos si el registro tiene la clave fecha_de_nacimiento y si su valor es igual a 1865
    if("fecha_de_nacimiento" in d):
        if(d["fecha_de_nacimiento"] == "1865"):

            # Si es así, creamos un nuevo diccionario y le añadimos id_BNE como clave y su correspondiente valor
            autor = {}
            autor['id_BNE'] = d["id_BNE"]

            # Añadimos el valor correpondiente a nombre_de_persona en el diccionario
            if("nombre_de_persona" in d):
                autor['nombre_de_persona'] = d["nombre_de_persona"]
            else:
                autor['nombre_de_persona'] = ''

            # Añadimos el valor correpondiente a género en el diccionario
            if("género" in d): 
                autor['género'] = d["género"]
            else:
                autor['género'] = ''

            # Añadimos a la lista de autores el diccionario creado
            autores.append(autor)

# Escribimos la cabecera del archivo csv, así como el listado de diccionario de autores y cerramos el fichero de salida    
escribir = csv.DictWriter(s, fieldnames=["id_BNE", "nombre_de_persona", "género"], delimiter=',')
escribir.writeheader()
escribir.writerows(autores)
s.close()





