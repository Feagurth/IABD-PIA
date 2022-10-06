# Realiza un programa que:
# Programa que va leyendo valores desde teclado y los va introduciendo en una lista hasta que se inserta un valor negativo. 
# Muestra todos los elementos introducidos en la lista en una única línea y separados estos por un espacio.

lista = []
numero = int(input("Introduzca un número entero. Introduzca un número negativo para salir: "))

while (numero >= 0):
    lista.append(numero)
    numero = int(input("Introduzca un número entero. Introduzca un número negativo para salir: "))

salida = ""
for i in range(0, len(lista)):
    salida += str(lista[i]) + " "

print(salida[:-1])
