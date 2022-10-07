# Realiza un programa que:
# Almacene el siguiente texto en una cadena de caracteres: 
# “Perdemos la juventud el día que dejamos de soñar con el paraíso en la tierra; el día que empezamos a llamar con desprecio utópicos a los que siguen soñando; el día que se nos despierta el sentido práctico y entramos en el juego y aceptamos las reglas.”. 
# A continuación, debe de recorrer la cadena e ir almacenando los caracteres que aparecen y el número de apariciones. Muestra por pantalla la información almacenada en el diccionario.
# Realiza lo mismo pero en esta ocasión se han de almacenar las palabras.

cadena = "Perdemos la juventud el día que dejamos de soñar con el paraíso en la tierra; el día que empezamos a llamar con desprecio utópicos a los que siguen soñando; el día que se nos despierta el sentido práctico y entramos en el juego y aceptamos las reglas."
cadenaLimpia = cadena.lower()
cadenaLimpia = cadenaLimpia.replace(",", "").replace(".", "").replace(";", "")
cadenaSinAcentos = cadenaLimpia.replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")

letras = {}
for letra in cadenaSinAcentos:
    if(letra != " "):
        if(letras.get(letra, -1) == -1):
            letras[letra] = 1
        else:
            letras[letra] += 1

palabras = {}
listaPalabras = cadenaLimpia.split(" ")

for palabra in listaPalabras:
    if(palabras.get(palabra, -1) == -1):
        palabras[palabra] = 1
    else:
        palabras[palabra] += 1

print(cadena)
print("")
print("El conteo de letras para la frase es de: ")
for letra in sorted(letras):
    print("%s: %s" % (letra.upper(), letras[letra]))

print("")
print("El conteo de palabras para la frase es de: ")
for palabra in sorted(palabras):
    print("%s: %s" % (palabra.capitalize(), palabras[palabra]))
