numero = int(input('diga um número e eu lhe direi o fatorial: '))

fatorial = 1

for n in range(2, numero + 1):
    fatorial *= n
    print(fatorial)
if n == 1: 
    print(fatorial)