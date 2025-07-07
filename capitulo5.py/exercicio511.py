numero = int(input('digite um número e eu direi se ele é triangular ou não: '))

triangular = False

lista = []
for n in range (1, numero + 1):
    if n * (n + 1) * (n + 2) == numero:
        triangular = True
        lista.extend([n, n + 1, n + 2])
        # usando extend no lugar de append para armazenar vários valores

if triangular:
    print(f'esse número é triangular pois {lista[0]} x {lista[1]} x {lista[2]} = {numero}')
else:
    print('esse número não é triangular!')