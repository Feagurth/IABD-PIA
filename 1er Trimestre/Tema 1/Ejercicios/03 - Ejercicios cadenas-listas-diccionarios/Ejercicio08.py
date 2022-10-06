# Realiza un programa que:
# Programa que nos pida por teclado el tamaño de una matriz (o una lista que contiene listas) de enteros y posteriormente lo recorra introduciendo valores aleatorios. 
# Los números han de estar comprendidos entre 1 y 100. Debe de mostrar la suma de los valores que hay en sus esquinas, así como el de sus dos diagonales. Ejemplo:
#   5   2  70  48    Laterales = 5 + 48 + 1 + 80
#   3   5   6  17    Diag. Principal = 5 + 5 + 6 +80
#  26   3   6   4    Diag. Secundaria = 48 + 6 + 3 + 1
#   1   1   2  80

import random


# Inicialización de variables
limiteSuperior = 100
limiteInferior = 1

laterales = 0
diagonalPrincipal = 0
diagonalSecundaria = 0
lstLaterales = []
lstDiagonal1 = []
lstDiagonal2 = []


# Petición de datos
lado = int(input("Introduzca el tamaño de la martiz cuadrada: "))
lista = []

for i in range(0, (lado * lado)):
    numero = random.randint(limiteInferior, limiteSuperior)
    lista.append(numero)

    # Condición: Si la columna es 0 o lado -1 y la fila es es 0 o lado -1
    if(((i // lado == 0) or (i // lado == (lado -1))) and (((i % lado) == 0) or ((i % lado) == (lado -1)))):
        laterales += numero
        lstLaterales.append(str(numero))

    # Condición: El número de columna y el número de fila son iguales
    if((i // lado) == (i % lado)):
        diagonalPrincipal += numero
        lstDiagonal1.append(str(numero))

    # Condición: El número de columna y el número de fila son iguales desde atrás
    if(((lado - 1) - (i // lado)) == (i % lado)):
        diagonalSecundaria += numero
        lstDiagonal2.append(str(numero))

salida = ""
contador = 0
# Impresión de la matriz generada
for i in range(0, len(lista)):
    salida += str(lista[i]).ljust(4)
    contador += 1

    if(contador >= lado):
        print(salida)
        contador = 0
        salida = ""

print("Laterales: [%s]: %d"  %(" + ".join(lstLaterales), laterales))
print("Diagonal principal: [%s]: %d"  %(" + ".join(lstDiagonal1), diagonalPrincipal))
print("Diagonal secundaria: [%s]: %d"  %(" + ".join(lstDiagonal2), diagonalSecundaria))