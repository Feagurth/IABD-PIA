# Escribe un programa que pida dos números por teclado, los almacene en 2 variables e intercambie el contenido de estas

numero1 = int(input("Introduzca un número entero: "))
numero2 = int(input("Introduzca otro número entero: "))

print("La variable numero1 vale", numero1, "y la variable numero2 vale", numero2)

apoyo = numero1
numero1 = numero2
numero2 = apoyo

print("Ahora la variable numero1 vale", numero1, "y la variable numero2 vale", numero2)