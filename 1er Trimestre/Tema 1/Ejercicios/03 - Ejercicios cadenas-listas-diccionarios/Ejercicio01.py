# Realiza un programa que:
# Lea una cadena de caracteres desde teclado y, posteriormente, la recorra mostrando por pantalla cada uno de los caracteres.

cadena = str(input("Introduzca una cadena de caracteres: "))

for i in range(0, len(cadena)):
    print("El caracter en la cadena en la posición %d es : %s" %(i, cadena[i]));
