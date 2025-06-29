numeros_digitados = int(input('digite quantos números serão digitados: '))

lista_valores = []

for n in range(1, numeros_digitados + 1):
    numeros = int(input(f'digite o {n}º valor: '))
    lista_valores.append(numeros)

media = (sum(lista_valores)) / numeros_digitados

print(f'a média do valores digitados é: {media}')

# página 64