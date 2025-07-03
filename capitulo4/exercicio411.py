lista_valores = []

for n in range(1, 11):
    valores = int(input(f'digite o {n}º valor: '))
    lista_valores.append(valores)

somatorio = sum(lista_valores)

media = somatorio / 10

print(f'a soma dos valores é: {somatorio} e a média é: {media}')