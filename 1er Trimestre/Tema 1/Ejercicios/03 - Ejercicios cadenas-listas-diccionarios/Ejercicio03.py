# Realiza un programa que:
# Lea una cadena desde teclado he indique cuantas palabras tiene dicho texto

cadena = str(input("Introduzca una cadena de caracteres: "))

cadena = cadena.replace(". ", " ").replace(", ", " ").replace("; ", " ").replace(".", " ").replace(",", " ").replace(";", " ")
palabras = cadena.split(" ")

print("El número de palabras de la cadena es: %d" %(len(palabras)))