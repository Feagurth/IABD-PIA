# Realiza un programa que:
# Introduzca en un diccionario las siglas de los módulos del experto de IA y big data y las horas que se imparten semanalmente. 
# Para finalizar debe de mostrar por pantalla tanto las siglas como las horas de cada módulo.

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

