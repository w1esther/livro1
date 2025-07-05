lista_idades = []
lista_alturas = []

for n in range (1, 6):
    idade = int(input(f'digite a idade da {n} ª pessoa: '))
    lista_idades.append(idade)

for n in range (1, 6):
    altura = int(input(f'digite a idade da {n}ª pessoa em cm: '))

# any armazena apenas os valores que atenderem à condição

existe_idade = any(n > 20 for n in lista_idades)

if not existe_idade:
    print('ninguém acima dos 20 anos')
else:
    media_idades = sum(existe_idade) / len(existe_idade)
    print(f'a média das idades maiores que 20 anos é: {media_idades}')

existe_altura = any(n < 170 for n in lista_alturas)

if not existe_altura:
    print('ninguém abaixo de 170 cm')
else:
    media_alturas = sum(existe_altura) / len(existe_altura)
    print(f'a média das alturas inferiores a 170 cm é: {media_alturas}')