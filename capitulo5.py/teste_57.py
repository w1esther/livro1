lista_pesos = []
lista_idades = []

for n in range(1, 7):
    peso = int(input(f'digite o pesso da {n}ª pessoa: '))
    lista_pesos.append(peso)
    idade = int(input(f'digite a idade da {n}ª pessoa: '))
    lista_idades.append(idade)

peso_menor_18 = [lista_pesos[n] for n in range(6) if lista_idades[n] < 18]

idade_mais_70 = [lista_idades[n] for n in range(6) if lista_pesos[n] > 70]

if not peso_menor_18:
    print('não há pessoas menores de 18 anos')
else:
    media_pesos = sum(peso_menor_18) / len(peso_menor_18)
    print(f'a média dos pesos das pessoas com menos de 18 anos é: {media_pesos}')

if not idade_mais_70:
    print('não há pessoas com mais de 70kg')
else:
    media_idade = sum(idade_mais_70) / len(idade_mais_70)
    print(f'a média das idadees das pessoas com mais de 70 kg é: {media_idade}')