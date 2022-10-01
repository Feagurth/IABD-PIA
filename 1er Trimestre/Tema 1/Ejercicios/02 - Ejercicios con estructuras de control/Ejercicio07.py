# Escriba un ejercicio que muestre la tabla de multiplicar de un número introducido por teclado

numero = int(input("Introduzca un número entero: "))

for i in range(1,11):
    print(numero," por", i, "es", str(numero * i))

