dia = int(input())
mes = int(input())
ano = int(input())
avanco = int(input())

if avanco < 32 and mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or 12:
    dia1 = dia + avanco
    print(f'{dia1}/{mes}/{ano}')
# ...