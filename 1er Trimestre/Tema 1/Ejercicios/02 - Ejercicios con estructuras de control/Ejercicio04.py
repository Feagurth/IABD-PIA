# Escribe un programa que reciba dos números desde teclado. Y realice una de las siguientes acciones:
#   1. Si el primer número es mayor que el segundo realice la resta.
#   2. Si el primer número es menor que el segundo realice la suma.
#   3. Si los números son iguales realice la multiplicación.

numero1 = int(input("Introduzca el primer número entero: "))
numero2 = int(input("Introduzca el segundo número entero: "))


if(numero1==numero2):
    print("La multiplicación de los dos números es", str(numero1*numero2))
else:
    if(numero1 > numero2):
        print("La resta de los dos números es", str(numero1-numero2))
    else:
        print("La suma de los dos números es", str(numero1+numero2))