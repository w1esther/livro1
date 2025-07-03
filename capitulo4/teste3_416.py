numero = int(input())

n1 = 2
n2 = 3

for n in range(3, numero + 1):
    expoente = (n +1)//2
    if n % 2 == 1:
        n3 = 2 ** (expoente)
    elif n % 2 == 0:
        n3 = 3 ** (expoente)

if numero == 1:
    print(n1)
elif numero == 2: 
    print(n2)
else:
    print(n3)