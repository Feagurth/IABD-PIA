#Escribe un ejercicio igual que el ejercicio 1 pero en el caso que sea cero el número introducido muestre por pantalla el mensaje: "el número es cero".
numero = int(input("Introduzca un número entero: "))

if(numero == 0):
    print("El número es cero")    
else:
    if( numero > 0):
        print("El número es positivo")
    else:
        print("El número es negativo")
