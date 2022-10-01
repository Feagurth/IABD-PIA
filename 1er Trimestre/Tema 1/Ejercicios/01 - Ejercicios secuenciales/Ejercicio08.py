# Escribe un programa que calcule a qué hora llegará un profesor desde el IES La Puebla al centro de formación. Para
# ello, solicitará la hora, minutos y segundos actuales y los segundos que emplea en realizar el
# trayecto

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