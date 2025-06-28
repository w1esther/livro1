inferior = int(input('entre com o valor de limite inferior: '))
superior = int(input('entre com o valor de limite superior: '))

somatorio = 0

for n in range (inferior, superior + 1):
    somatorio += n

print(f'a soma entre todos os valores entre {inferior} e {superior} é: {somatorio}')