# Realiza un programa que: 
# Programa que pida un valor “n” que será el tamaño de dos listas, las cuales habrá que rellenar con números enteros entre 1 y 100. 
# Posteriormente, tiene que comprobar si tienen algún elemento en común e indicarlo por pantalla.
# Por ejemplo: si la primera lista tiene los valores “3, 48, 5, 6” y el segundo “7, 99, 100, 48” indicará que si hay elementos en común ya que ambos tienen el número 48.
import random

limiteSuperior = 100
limiteInferior = 0

lista1 = []
lista2 = []
numero = int(input("Introduzca el número de elementos a generar: "))
print("Se generaran 2 listas de %d número(s) aleatorio(s) entre %d y %d" %(numero, limiteInferior, limiteSuperior))

for i in range(0, numero):
    numero = random.randint(limiteInferior, limiteSuperior)
    lista1.append(str(numero))
    numero = random.randint(limiteInferior, limiteSuperior)
    lista2.append(str(numero))

diferencias = list((set(lista1) & set(lista2)))

print("Los números generados en la primera lista son: [%s]" %(", ".join(lista1)))
print("Los números generados en la segunda lista son: [%s]" %(", ".join(lista2)))

if(len(diferencias) > 0):
    print("Los números repetidos en ambas listas son: [%s]" %(", ".join(diferencias)))
else:
    print("No hay números repetidos en las dos listas")

