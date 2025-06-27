hora = int(input('digite o valor das horas: '))
minuto = int(input('digite o valor dos minutos: '))
segundos = int(input('digite o valor dos segundos: '))

segundos_passados = (hora * 3600) + (minuto * 60) + segundos

print(f'os segundos passados desde a última meia-noite da hora lida foram {segundos_passados} segundos')