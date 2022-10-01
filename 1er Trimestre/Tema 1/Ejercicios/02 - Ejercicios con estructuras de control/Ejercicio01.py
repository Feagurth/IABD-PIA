#Escribe un programa que indique si el número introducido desde teclado es positivo o negativo mostrando un mensaje por pantalla. El cero lo consideraremos como número positivo.

numero = int(input("Introduzca un número entero: "))

if( numero >= 0):
    print("El número es positivo")
else:
    print("El número es negativo")
    