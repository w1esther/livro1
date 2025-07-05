lista_idades = []

for n in range (1, 11):
    idades = int(input(f'digite a {n}ª idade: '))
    lista_idades.append(idades)

quantidade = sum(1 for n in lista_idades if n >= 18)

print(f'{quantidade} pessoas são maiores de idade!')