# Escribe un programa que introducido un número indique si es positivo. Si no lo es finalizará el
# programa pero en caso de que sea mayor que cero mostrará todos los números entre los que
# es divisible.
# Ejemplo: si se introduce el 20 mostrará: 10, 5, 4, 2 y 1.

numero = int(input("Introduzca un número entero: "))

if(numero <= 0):
    print("El número no es positivo")
else:
    for i in range((numero - 1), 0, -1):
        if((numero % i) == 0):
            print("El número", numero, "es divisible entre", i)