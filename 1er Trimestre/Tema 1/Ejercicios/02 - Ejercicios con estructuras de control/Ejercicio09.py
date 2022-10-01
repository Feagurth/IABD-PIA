# Escriba un programa que compruebe que el número introducido desde teclado esté entre 1 y 12,
# ambos inclusive. En caso de que el valor no esté en este intervalo ha de mostrar un mensaje
# de error y volver a solicitar al usuario que introduzca nuevamente un número. Este proceso
# se ha de repetir mientras no se cumpla esta condición

numero = int(input("Introduzca un número entero entre 1 y 12 ambos inclusive: "))

while (numero < 1 or numero > 12):
    numero = int(input("Introduzca un número entero entre 1 y 12 ambos inclusive: "))

print("El número introducido es", numero)