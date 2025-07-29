somatorio = 0
while True:
    pesos = float(input('digite o peso da pessoa: '))
    peso_total = somatorio + pesos
    while peso_total >= 500:
        print('carga máxima atingida')
    break