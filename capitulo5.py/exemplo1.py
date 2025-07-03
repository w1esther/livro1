casas_decimais = 2
precisao = 10 ** -casas_decimais
x = float(input())
y = float(input())
if abs(x-y) < precisao: # comparar números de ponto flutuante (decimais)
    print('os números são iguais')
else:
    print('os números são diferentes')