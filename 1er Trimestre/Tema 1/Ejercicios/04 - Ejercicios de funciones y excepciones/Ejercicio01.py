# Crea un módulo de Python que contenga todos los ejercicios creados en las sesiones anteriores. Para
# ello, crea una función para cada uno de ellos. Debes de controlar las posibles excepciones que se
#puedan dar

def t1_e01():
    """ Escribe un programa que Diga ¡hola mundo! """
    print("¡hola mundo!")

def t1_e02():
    """ Escribe un programa que pida un nombre y lo salude. """
    nombre = input("¿Cual es tu nombre? ")
    print("Saludos", nombre)

def t1_e03():
    """ Escribe un programa que pida un número y lo muestre por pantalla. El número ha de almacenarlo en una variable. """
    try:
        numero = int(input("Introduce un número: "))
        print("El número introducido es el", numero)
    except ValueError:
        print("Error!. El valor introducido no es un número entero")

def t1_e04():
    """ Escribe un programa que pida dos números enteros, realice la suma y la muestre por pantalla """
    try:
        numero1 = int(input("Introduzca el primer número entero: "))
        numero2 = int(input("Introduzca el segundo número entero: "))
        
        resultado = int(numero1) + int(numero2)
        print("La suma de los dos números es:", resultado)
    except ValueError:
        print("Error!. El valor introducido no es un número entero")

def t1_e05():
    """ Escribe un programa que pida la base y la altura de un rectángulo en milímetros y muestre el área del mismo. """
    try: 
        base =float(input("Introduzca la longitud de la base en milímetros: "))
        altura = float(input("Introduzca la longitud de la altura en milímetros: "))
        area = ((base * altura))/2

    except ValueError:
        print("Error!. El valor introducido no es un número decimal")
    else:
        print("El area del triángulo es: ", area)

def t1_e06():
    """ Escribe un programa que realice todas las operaciones aritméticas de dos números introducidos por teclado. """
    try: 
        numero1 = int(input("Introduzca el primer número entero: "))
        numero2 = int(input("Introduzca el segundo número entero: "))
    
        print("La suma de los dos números es: ", (numero1 + numero2))
        print("La resta de los dos números es: ", (numero1 - numero2))
        print("La multiplicación de los dos números es: ", (numero1 * numero2))
        print("La división de los dos números es: ", (numero1 / numero2))
        print("La división entera de los dos números es: ", (numero1 // numero2))
        print("La división modulo de la división de los dos números es: ", (numero1 % numero2))
        print("La potencia de los dos números es: ", (numero1 ** numero2))
    except ValueError:
        print("Error!. El valor introducido no es un número entero")

def t1_e07():
    """ Escribe un programa que pida 5 números y calcule su media. """

    try:
        numero1 = int(input("Introduzca el primer número entero: "))
        numero2 = int(input("Introduzca el segundo número entero: "))
        numero3 = int(input("Introduzca el tercer número entero: "))
        numero4 = int(input("Introduzca el cuarto número entero: "))
        numero5 = int(input("Introduzca el quinto número entero: "))
        media = ((numero1 + numero2 + numero3 + numero4 + numero5) /5)

        print("La media de los cinco números introducidos es:", media)
    except ValueError:
        print("Error!. El valor introducido no es un número entero")        

def t1_e08():
    """ Escribe un programa que calcule a qué hora llegará un profesor desde el IES La Puebla al centro de formación. Para
    ello, solicitará la hora, minutos y segundos actuales y los segundos que emplea en realizar el
    trayecto """
    try:
        horasActuales = int(input("Introduzca la hora actual (0-24): "))
        minutosActuales = int(input("Introduzca los minutos actuales en formato (0-60): "))
        segundosActuales = int(input("Introduzca los segundos actuales en formato (0-60): "))

        segundosTrayecto = int(input("Introduzca los segundos tarda el profesor en realizar el trayecto: "))

        segundosTotales = (horasActuales * 3600) + (minutosActuales * 60) + segundosActuales + segundosTrayecto

        horasLlegada = (segundosTotales // 3600)
        segundosTotales = segundosTotales - (horasLlegada * 3600)
        minutosLlegada = (segundosTotales // 60)
        segundosLlegada = segundosTotales - (minutosLlegada * 60)

        print("La hora de llegada del profesor sera a :", f'{horasLlegada:02}' + ":" + f'{minutosLlegada:02}' + ":" + f'{segundosLlegada:02}')
    except ValueError:
        print("Error!. El valor introducido no es un número entero")        

def t1_e09():
    """ Escribe un programa que pida dos números por teclado, los almacene en 2 variables e intercambie el contenido de estas """

    try:
        numero1 = int(input("Introduzca un número entero: "))
        numero2 = int(input("Introduzca otro número entero: "))

        print("La variable numero1 vale", numero1, "y la variable numero2 vale", numero2)

        apoyo = numero1
        numero1 = numero2
        numero2 = apoyo

        print("Ahora la variable numero1 vale", numero1, "y la variable numero2 vale", numero2)    
    except ValueError:
        print("Error!. El valor introducido no es un número entero")

def t1_e10():
    """ Piensa en dos ejercicios secuenciales distintos de los anteriores. Escribe el enunciado y, si quieres, resuelvelos.
    Escribe un programa que data la altura de un cubo calcule su volumen """

    try:
        lado = int(input("Introduzca un número entero para la longitud del lado del cubo en centíimetros: "))
        print("El volumen del cubo es:", lado**3, "cm³")

        """ Escribe un programa que introducido un numero de dos cifras le de la vuelta -> 23 pasa a 32 """

        numero = int(input("Introduzca un número entero de dos cifras: (10-99): "))

        if(len(str(numero)) != 2):
            raise Exception("Error!. El valor introducido debe tener dos dígitos")

        decenas = numero // 10
        unidades = numero % 10

        print("El numero introducido era", numero, "y el numero invertido es:",  str(unidades) + str(decenas))    
    except ValueError:
        print("Error!. El valor introducido no es un número entero")
    except Exception as e:
        print(e.args[0])
    
def t2_e01():
    """ Escribe un programa que indique si el número introducido desde teclado es positivo o negativo mostrando un mensaje por pantalla. 
    El cero lo consideraremos como número positivo. """

    try:
        numero = int(input("Introduzca un número entero: "))

        if( numero >= 0):
            print("El número es positivo")
        else:
            print("El número es negativo")
    except ValueError:
        print("Error!. El valor introducido no es un número entero")
    
def t2_e02():
    """ Escribe un ejercicio igual que el ejercicio 1 pero en el caso que sea cero el número introducido muestre por pantalla el mensaje: "el número es cero". """

    try:         
        numero = int(input("Introduzca un número entero: "))

        if(numero == 0):
            print("El número es cero")    
        else:
            if( numero > 0):
                print("El número es positivo")
            else:
                print("El número es negativo")
    except ValueError:
        print("Error!. El valor introducido no es un número entero")

def t2_e03():
    """ Escribe un programa que indique cuál es el mayor de dos números introducidos por teclado. Si son iguales también ha de notificarlo. """

    try:
        numero1 = int(input("Introduzca el primer número entero: "))
        numero2 = int(input("Introduzca el segundo número entero: "))

        if(numero1 == numero2):
            print("Los dos números introducidos son iguales")
        else:
            if(numero1 > numero2):
                print("El primer número, " + str(numero1) + ", es mayor  que el segundo número, " + str(numero2))
            else:
                print("El segundo número, " + str(numero2) + ", es mayor  que el primer número, " + str(numero1))
    except ValueError:
        print("Error!. El valor introducido no es un número entero")

def t2_e04():
    """ Escribe un programa que reciba dos números desde teclado. Y realice una de las siguientes acciones:
    1. Si el primer número es mayor que el segundo realice la resta.
    2. Si el primer número es menor que el segundo realice la suma.
    3. Si los números son iguales realice la multiplicación. """

    try:
        numero1 = int(input("Introduzca el primer número entero: "))
        numero2 = int(input("Introduzca el segundo número entero: "))

        if(numero1==numero2):
            print("La multiplicación de los dos números es", str(numero1*numero2))
        else:
            if(numero1 > numero2):
                print("La resta de los dos números es", str(numero1-numero2))
            else:
                print("La suma de los dos números es", str(numero1+numero2))
    except ValueError:
        print("Error!. El valor introducido no es un número entero")

def t2_e05():
    """ Escribe un programa que muestre los 30 primeros números enteros. """
    for i in range (0, 30):
        print(i)    

def t2_e06():
    """ Escribe un programa que muestre los números impares que hay entre el 200 y el 289. """

    for i in range(200, 290):
        if(i % 2 == 1):
            print(i)

def t2_e07():
    """ Escriba un ejercicio que muestre la tabla de multiplicar de un número introducido por teclado """
    
    try:
        numero = int(input("Introduzca un número entero: "))
        for i in range(1,11):
            print(numero,"x", i, "=", str(numero * i))

    except ValueError:
        print("Error!. El valor introducido no es un número entero")

def t2_e08():
    """ Escriba un programa que realice la suma de los números comprendidos entre 7 y 256 y muestre el resultado por pantalla """

    contador = 0
    for i in range(7, 257):
        contador += i

    print("El resultado de sumar los númreos comprendidos entre 7 y 256 es:", contador)    

def t2_e09():
    """ Escriba un programa que compruebe que el número introducido desde teclado esté entre 1 y 12, 
    ambos inclusive. En caso de que el valor no esté en este intervalo ha de mostrar un mensaje 
    de error y volver a solicitar al usuario que introduzca nuevamente un número. Este proceso 
    se ha de repetir mientras no se cumpla esta condición """

    try:
        numero = int(input("Introduzca un número entero entre 1 y 12 ambos inclusive: "))

        while (numero < 1 or numero > 12):
            numero = int(input("Introduzca un número entero entre 1 y 12 ambos inclusive: "))

        print("El número introducido es", numero)

    except ValueError:
        print("Error!. El valor introducido no es un número entero")        

def t2_e10():
    """ Escribe un programa que introducido un número indique si es positivo. Si no lo es finalizará el 
    programa pero en caso de que sea mayor que cero mostrará todos los números entre los que
    es divisible.
    Ejemplo: si se introduce el 20 mostrará: 10, 5, 4, 2 y 1. """

    try:
        numero = int(input("Introduzca un número entero: "))

        if(numero <= 0):
            print("El número no es positivo")
        else:
            for i in range((numero - 1), 0, -1):
                if((numero % i) == 0):
                    print("El número", numero, "es divisible entre", i)    

    except ValueError:
        print("Error!. El valor introducido no es un número entero")        

def t3_e01():
    """ Realiza un programa que:
    Lea una cadena de caracteres desde teclado y, posteriormente, la recorra mostrando por pantalla cada uno de los caracteres. """

    try:
        cadena = str(input("Introduzca una cadena de caracteres: "))

        if(len(cadena) == 0):
            raise Exception("La cadena debe ser distinta de vacío")

        for i in range(0, len(cadena)):
            print("El caracter en la cadena en la posición %d es : %s" %(i, cadena[i]));
    
    except Exception as e:
        print(e.args[0])

def t3_e02():
    """ Realiza un programa que:
    Lea una cadena desde teclado y una palabra. Indique cuantas veces aparece dicha palabra. """

    try:
        cadena = str(input("Introduzca una cadena de caracteres: "))
        palabra = str(input("Introduzca una palabra para buscar en la cadena: "))

        if(len(cadena) == 0):
            raise Exception("La cadena debe ser distinta de vacío")

        if(len(palabra) == 0):
            raise Exception("La palabra debe ser distinta de vacío")            

        if(len(cadena) < len(palabra)):
            raise Exception("La longitud de la cadena no puede ser menor que la longitud de palabra")

        repeticiones = len(cadena.lower().split(palabra.lower())) - 1

        print("La palabra %s estaba %d veces en cadena %s" %(palabra, repeticiones, cadena))

    except Exception as e:
        print(e.args[0])

def t3_e03():
    """ Realiza un programa que:
    Lea una cadena desde teclado he indique cuantas palabras tiene dicho texto """

    try:

        cadena = str(input("Introduzca una cadena de caracteres: "))

        if(len(cadena) == 0):
            raise Exception("La cadena debe ser distinta de vacío")

        cadena = cadena.replace(". ", " ").replace(", ", " ").replace("; ", " ").replace(".", " ").replace(",", " ").replace(";", " ")
        palabras = cadena.split(" ")

        print("El número de palabras de la cadena es: %d" %(len(palabras)))

    except Exception as e:
        print(e.args[0])

def t3_e04():
    """ Realiza un programa que: 
    Crea una lista con 10 elementos y haz que se rellene con los 10 primeros números pares mediante un bucle. Muestra a continuación los valores almacenados. """

    lista = []

    for i in range(1, 21):
        if(i % 2 == 0):
            lista.append(i)

    for i in range(0, len(lista)):
        print("El valor de la posición %d es : %d" %(i+1, lista[i]))

def t3_e05():
    """ Realiza un programa que:
    Programa que va leyendo valores desde teclado y los va introduciendo en una lista hasta que se inserta un valor negativo. 
    Muestra todos los elementos introducidos en la lista en una única línea y separados estos por un espacio. """

    try:
        lista = []
        numero = int(input("Introduzca un número entero. Introduzca un número negativo para salir: "))

        while (numero >= 0):
            lista.append(numero)
            numero = int(input("Introduzca un número entero. Introduzca un número negativo para salir: "))

        salida = ""
        for i in range(0, len(lista)):
            salida += str(lista[i]) + " "

        print(salida[:-1])

    except ValueError:
        print("Error!. El valor introducido no es un número entero")        

def t3_e06():
    """ Realiza un programa que: 
    Programa que pida por teclado la cantidad de elementos de la lista y posteriormente lo recorra introduciendo valores aleatorios. 
    Después, ha de obtener la media de todos los números introducidos, el número más alto y el más bajo que hay en la lista """

    import random

    limiteSuperior = 1000
    limiteInferior = 0
    mayor = limiteInferior
    menor = limiteSuperior
    contador = 0

    lista = []

    try:

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

    except ValueError:
        print("Error!. El valor introducido no es un número entero")        
    
def t3_e07():
    """ Realiza un programa que: 
    Programa que pida un valor “n” que será el tamaño de dos listas, las cuales habrá que rellenar con números enteros entre 1 y 100. 
    Posteriormente, tiene que comprobar si tienen algún elemento en común e indicarlo por pantalla. 
    Por ejemplo: si la primera lista tiene los valores “3, 48, 5, 6” y el segundo “7, 99, 100, 48” indicará que si hay elementos en común ya que ambos tienen el número 48. """

    import random

    limiteSuperior = 100
    limiteInferior = 0

    lista1 = []
    lista2 = []

    try:
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

    except ValueError:
        print("Error!. El valor introducido no es un número entero")        

def t3_e08():
    """ Realiza un programa que: 
    Programa que nos pida por teclado el tamaño de una matriz (o una lista que contiene listas) de enteros y posteriormente lo recorra introduciendo valores aleatorios. 
    Los números han de estar comprendidos entre 1 y 100. Debe de mostrar la suma de los valores que hay en sus esquinas, así como el de sus dos diagonales. Ejemplo: 
     5   2  70  48    Laterales = 5 + 48 + 1 + 80 
     3   5   6  17    Diag. Principal = 5 + 5 + 6 +80 
    26   3   6   4    Diag. Secundaria = 48 + 6 + 3 + 1 
     1   1   2  80 """

    import random

    # Inicialización de variables
    limiteSuperior = 100
    limiteInferior = 1

    laterales = 0
    diagonalPrincipal = 0
    diagonalSecundaria = 0
    lstLaterales = []
    lstDiagonal1 = []
    lstDiagonal2 = []

    try:

        # Petición de datos
        lado = int(input("Introduzca el tamaño de la martiz cuadrada: "))
        lista = []

        for i in range(0, (lado * lado)):

            numero = random.randint(limiteInferior, limiteSuperior)
            lista.append(numero)

            columna = (i // lado)
            fila = (i % lado)

            # Condición: Si la columna es 0 o lado - 1 y la fila es es 0 o lado - 1
            if(((columna == 0) or (columna == (lado - 1))) and (((fila) == 0) or ((fila) == (lado - 1)))):
                laterales += numero
                lstLaterales.append(str(numero))

            # Condición: El número de columna y el número de fila son iguales
            if((columna) == (fila)):
                diagonalPrincipal += numero
                lstDiagonal1.append(str(numero))

            # Condición: El número de columna y el número de fila son iguales desde atrás
            if(((lado - 1) - (columna)) == (fila)):
                diagonalSecundaria += numero
                lstDiagonal2.append(str(numero))

        salida = ""
        contador = 0
        # Impresión de la matriz generada
        for i in range(0, len(lista)):
            salida += str(lista[i]).rjust(4)
            contador += 1

            if(contador >= lado):
                print(salida)
                contador = 0
                salida = ""

        print("Laterales: [%s]: %d"  %(" + ".join(lstLaterales), laterales))
        print("Diagonal principal: [%s]: %d"  %(" + ".join(lstDiagonal1), diagonalPrincipal))
        print("Diagonal secundaria: [%s]: %d"  %(" + ".join(lstDiagonal2), diagonalSecundaria))    

    except ValueError:
        print("Error!. El valor introducido no es un número entero")                

def t3_e09():
    """ Realiza un programa que: 
    Introduzca en un diccionario las siglas de los módulos del experto de IA y big data y las horas que se imparten semanalmente. 
    Para finalizar debe de mostrar por pantalla tanto las siglas como las horas de cada módulo. """

    cursos = {}

    cursos[("SSA", "Sistemas de Aprendizaje Automatico")] = {("Lunes", "16:00-19:00")}
    cursos[("SBD", "Sistemas de Big Data")] = {("Lunes", "19:00-22:00")}
    cursos[("BDA", "Big Data Aplicado")] = {("Miercoles", "14:00-19:00"), ("Jueves", "19:00-20:00")}
    cursos[("PIA", "Programacion de Inteligencia Artificial")] = {("Miercoles", "19:00-22:00"), ("Jueves", "16:00-18:00")}
    cursos[("MIA", "Modelos de Inteligencia Artificial")] = {("Jueves", "20:00-22:00")}

    print("")
    for curso in cursos:
        horarios = cursos[curso]
        print("%s: %s" %(curso[0], curso[1]))
        for horario in horarios:
            print("%s - %s" %(horario[0].rjust(12), horario[1]))
        print("")

def t3_e10():
    """ Realiza un programa que: 
    Almacene el siguiente texto en una cadena de caracteres: 
    “Perdemos la juventud el día que dejamos de soñar con el paraíso en la tierra; el día que empezamos a llamar con desprecio utópicos a los que siguen soñando; el día que se nos despierta el sentido práctico y entramos en el juego y aceptamos las reglas.”. 
    A continuación, debe de recorrer la cadena e ir almacenando los caracteres que aparecen y el número de apariciones. Muestra por pantalla la información almacenada en el diccionario. 
    Realiza lo mismo pero en esta ocasión se han de almacenar las palabras. """

    cadena = "Perdemos la juventud el día que dejamos de soñar con el paraíso en la tierra; el día que empezamos a llamar con desprecio utópicos a los que siguen soñando; el día que se nos despierta el sentido práctico y entramos en el juego y aceptamos las reglas."
    cadenaLimpia = cadena.lower()
    cadenaLimpia = cadenaLimpia.replace(",", "").replace(".", "").replace(";", "")
    cadenaSinAcentos = cadenaLimpia.replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")

    letras = {}
    for letra in cadenaSinAcentos:
        if(letra != " "):
            if(letras.get(letra, -1) == -1):
                letras[letra] = 1
            else:
                letras[letra] += 1

    palabras = {}
    listaPalabras = cadenaLimpia.split(" ")

    for palabra in listaPalabras:
        if(palabras.get(palabra, -1) == -1):
            palabras[palabra] = 1
        else:
            palabras[palabra] += 1

    print(cadena)
    print("")
    print("El conteo de letras para la frase es de: ")
    for letra in sorted(letras):
        print("%s: %s" % (letra.upper(), letras[letra]))

    print("")
    print("El conteo de palabras para la frase es de: ")
    for palabra in sorted(palabras):
        print("%s: %s" % (palabra.capitalize(), palabras[palabra]))

t3_e08()