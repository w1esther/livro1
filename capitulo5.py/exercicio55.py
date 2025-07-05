lista_impares = []
lista_pares = []

for n in range (1, 11):
    numeros = int(input(f'digite o {n}º número: '))
    if numeros % 2 == 0:
        lista_pares.append(numeros)
    else:
        lista_impares.append(numeros)

# somo todos os elementos da lista e divido pela quantidade de elementos somados (quantidade de elementos da lista)

media_impares = sum(lista_impares) / len(lista_impares)

media_pares = sum(lista_pares) / len(lista_pares)

print(f'a média dos números pares digitados é: {media_pares} \na média dos números ímpares digitados é: {media_impares}')