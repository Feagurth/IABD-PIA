# Piensa en dos ejercicios secuenciales distintos de los anteriores. Escribe el enunciado y, si quieres, resuelvelos.
# Escribe un programa que data la altura de un cubo calcule su volumen

lado = int(input("Introduzca un número entero para la longitud del lado del cubo en centíimetros: "))
print("El volumen del cubo es:", lado**3, "cm³")

#Escribe un programa que introducido un numero de dos cifras le de la vuelta -> 23 pasa a 32

numero = int(input("Introduzca un número entero de dos cifras: (10-99): "))

decenas = numero // 10
unidades = numero % 10

print("El numero introducido era", numero, "y el numero invertido es:",  str(unidades) + str(decenas))