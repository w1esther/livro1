numero = int(input())

n1 = 1 
n2 = 1

if numero == 1 or numero == 2:
    print(n1)
else:
    for n in range(3, numero + 1):
        n3 = (n2 ** 2) + (n1 ** 3)
        n1 = n2
        n2 = n3
    print(n3)