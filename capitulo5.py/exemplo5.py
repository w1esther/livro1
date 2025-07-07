numero = int(input('digite um número e eu direi se ele é primo ou não: '))

lista = []
for n in range (2, numero//2 + 1):
    if numero % n == 0:
        lista.append(n)
    
if lista == []:
    print('esse número é primo!')
else: 
    print('esse número não é primo!')