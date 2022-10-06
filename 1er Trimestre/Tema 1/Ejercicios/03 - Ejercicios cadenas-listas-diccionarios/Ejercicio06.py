# Realiza un programa que: 
# Programa que pida por teclado la cantidad de elementos de la lista y posteriormente lo recorra introduciendo valores aleatorios. 
# Después, ha de obtener la media de todos los números introducidos, el número más alto y el más bajo que hay en la lista
import random

limiteSuperior = 1000
limiteInferior = 0
mayor = limiteInferior
menor = limiteSuperior
contador = 0

lista = []

numero = int(input("Introduzca el número de elementos a generar: "))
print("Se generaran %d número(s) aleatorio(s) entre %d y %d" %(numero, limiteInferior, limiteSuperior))

for i in range(0, numero):
    numero = random.randint(limiteInferior, limiteSuperior)
    lista.append(str(numero))
    
    if(numero > mayor):
        mayor = numero

    if(numero < menor):
        menor = numero
    
    contador += numero

print("Los números generados fueron: [%s]" %(", ".join(lista)))
print("El mayor número generado es %d y el menor es %d" %(mayor, menor))
print("La media de todos los valores generados es: %.2f" %(contador/len(lista)))
