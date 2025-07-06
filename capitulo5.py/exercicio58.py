numero = int(input('digite um número e eu direi se ele é perfeito ou não: '))

divisores = []

for n in range (1, numero):
    if numero % n == 0: 
        divisores.append(n)

if sum(divisores) == numero:
    print('esse número é PERFEITO')
else: 
    print('esse número não é perfeito...')