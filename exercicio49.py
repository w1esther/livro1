n = int(input('digite um número: '))

somatorio = 0

for i in range(1, n+1):
    somatorio += i ** 2
    
print(somatorio)