lista = []

for n in range(1, 11):
    num = float(input(f'digite o {n}º número:'))
    lista.append(num)

maior = max(lista)

print(f'o maior número da lista é: {maior}')
