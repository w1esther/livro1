lista_impares = []
lista_pares = []

for n in range (1, 11):
    numeros = int(input(f'digite o {n}º número: '))
    if numeros % 2 == 0:
        lista_pares.append(numeros)
    else:
        lista_impares.append(numeros)

# somo todos os elementos da lista e divido pela quantidade de elementos somados (quantidade de elementos da lista)

# uma lista vazia é: []

# ateção na escrita lógica dos prints

if lista_impares == []:
    print('não foi possível calcular a média dos números ímpares pois nenhum ímpar foi informado!')
else:
    media_impares = sum(lista_impares) / len(lista_impares)

if lista_pares == []:
    print('não é possível calcular a média dos números pares pois nenhum par foi informado!')
else:
    media_pares = sum(lista_pares) / len(lista_pares)

if lista_pares != [] and lista_impares != []:
    print(f'a média dos números pares digitados é: {media_pares} \na média dos números ímpares digitados é: {media_impares}')
elif lista_pares != [] and lista_impares == []:
    print(f'a média dos números pares é: {media_pares}')
elif lista_pares == [] and lista_impares != []:
    print(f'a média dos números ímpares é: {media_impares}')