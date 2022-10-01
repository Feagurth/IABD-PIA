# Escribe un programa que indique cuál es el mayor de dos números introducidos por teclado. Si son iguales también ha de notificarlo.

numero1 = int(input("Introduzca el primer número entero: "))
numero2 = int(input("Introduzca el segundo número entero: "))

if(numero1 == numero2):
    print("Los dos números introducidos son iguales")
else:
    if(numero1 > numero2):
        print("El primer número, " + str(numero1) + ", es mayor  que el segundo número, " + str(numero2))
    else:
        print("El segundo número, " + str(numero2) + ", es mayor  que el primer número, " + str(numero1))