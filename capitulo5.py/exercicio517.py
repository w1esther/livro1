nota = float(input('digite sua nota: '))

if nota > 10 or nota < 0:
    print('nota inválida!')
elif nota == 9 or nota == 10:
    print('A')
elif nota > 7.999 and nota < 9:
    print('B')
elif nota > 6.999 and nota < 8:
    print('C')
elif nota < 7:
    print('E')