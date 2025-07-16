lista = []

for n in range(1, 11):
    voto = int(input(f'voto do {n}º eleitor: '))
    lista.append(voto)

abel = beatriz = caio = dirce = eustaquio = brancos = nulos = 0

for n in lista:
    if n == 11:
        abel += 1
    elif n == 15:
        beatriz += 1 
    elif n == 21:
        caio += 1
    elif n == 25:
        dirce += 1
    elif n == 46:
        eustaquio += 1
    elif n == 0:
        brancos += 1
    else:
        nulos += 1

print(f'abel: {abel}')
print(f'beatriz: {beatriz}')
print(f'caio: {caio}')
print(f'dirce: {dirce}')
print(f'eustáquio: {eustaquio}')
print(f'brancos: {brancos}')
print(f'nulos: {nulos}')