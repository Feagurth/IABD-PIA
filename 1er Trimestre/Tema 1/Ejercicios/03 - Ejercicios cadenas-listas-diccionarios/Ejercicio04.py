# Realiza un programa que: 
# Crea una lista con 10 elementos y haz que se rellene con los 10 primeros números pares mediante un bucle. Muestra a continuación los valores almacenados.
lista = []

for i in range(1, 21):
    if(i % 2 == 0):
        lista.append(i)

for i in range(0, len(lista)):
    print("El valor de la posición %d es : %d" %(i+1, lista[i]))
