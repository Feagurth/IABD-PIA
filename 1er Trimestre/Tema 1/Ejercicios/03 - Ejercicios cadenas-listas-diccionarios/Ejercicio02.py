# Realiza un programa que:
# Lea una cadena desde teclado y una palabra. Indique cuantas veces aparece dicha palabra.

cadena = str(input("Introduzca una cadena de caracteres: "))
palabra = str(input("Introduzca una palabra para buscar en la cadena: "))

repeticiones = len(cadena.lower().split(palabra.lower())) - 1

print("La palabra %s estaba %d veces en cadena %s" %(palabra, repeticiones, cadena))
