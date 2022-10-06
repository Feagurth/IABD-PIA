# Realiza un programa que:
# Programa que nos pida por teclado el tamaño de una matriz (o una lista que contiene listas) de enteros y posteriormente lo recorra introduciendo valores aleatorios. 
# Los números han de estar comprendidos entre 1 y 100. Debe de mostrar la suma de los valores que hay en sus esquinas, así como el de sus dos diagonales. Ejemplo:
#   5   2  70  48    Laterales = 5 + 48 + 1 + 80
#   3   5   6  17    Diag. Principal = 5 + 5 + 6 +80
#  26   3   6   4    Diag. Secundaria = 48 + 6 + 3 + 1
#   1   1   2  80



import random

salida = ""
contador = 0

limiteSuperior = 100
limiteInferior = 1

laterales = 0

lado = int(input("Introduzca el tamaño de la martiz cuadrada: "))
lista = []

for i in range(1, (lado * lado)+1):
    numero = random.randint(limiteInferior, limiteSuperior)
    lista.append(numero)

    if((((i % (lado * lado)) == 1) or (i % (lado * lado) == 0)) and ((i / (lado * lado) == 0) or (i / (lado * lado)) >= (lado * lado) -1 )):
        laterales += numero


# Impresión de la matriz generada
for i in range(1, len(lista) + 1):
    salida += str(lista[i - 1]).ljust(4)
    contador += 1

    if(contador != 1 and (len(lista)) % contador == 0):
        print(salida)
        contador = 0
        salida = ""