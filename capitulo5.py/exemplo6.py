numero = int(input('digite um número e eu direi se ele é primo ou não: '))

primo = True
for n in range (2, numero//2 + 1):
    if numero % n == 0:
        primo = False

if primo:
    print('é primo!')
else:
    print('não é primo!')