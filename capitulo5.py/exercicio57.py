lista_idades = []
lista_alturas = []

for n in range (1, 6):
    idade = int(input(f'digite a idade da {n} ª pessoa: '))
    lista_idades.append(idade)
    altura = int(input(f'digite a altura da {n}ª pessoa em cm: '))
    lista_alturas.append(altura)

idades_menor_170 = [lista_idades[n] for n in range(5) if lista_alturas[n] < 170]

altura_maiores_20 = [lista_alturas[n] for n in range (5) if lista_idades[n] > 20]

if not idades_menor_170:
    print('ninguém abaixo de 170cm')
else:
    media_idade = sum(idades_menor_170) / len(idades_menor_170)
    print(f'a média das idades das pessoas com altura inferior a 170cm é: {media_idade}')

if not altura_maiores_20:
    print('não há pessoas com mais de 20 anos')
else: 
    media_altura = sum(altura_maiores_20) / len(altura_maiores_20)
    print(f'a altura média das pessoas com mais de 20 anos é: {media_altura}')