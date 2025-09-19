dias = float(input("quantidade de dias: "))
horas = float(input("quantidade de horas: "))
minutos = float(input("quantidade de minutos: "))
segundos = float(input("quantidade de segundos: "))

dia_segundos = dia * 86400
hora_segundos = hora * 3600
minuto_segundos = minuto * 60

total_segundos = dias_segundos + hora_segundos + minutos_segundos + segundo
print(f"Total em segundos é: {total_segundos}")