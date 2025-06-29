numero = int(input())

n1 = 2

if numero == 1:
    print(n1)
else:
    for n in range(2, numero + 1):
        if n % 3 == 0:
            n1 = n1 ** 2
        elif n % 2 == 0:
            n1 = n1 + 5
        else: 
            n1 = n1 * 2
    print(n1)
