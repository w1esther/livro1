numero = int(input())

n1 = 1
n2 = 2

if numero == 1:
    print(n1)
elif numero == 2:
    print(n2)
else: 
    for n in range(3, numero + 1):
        if n % 2 == 0: 
            n3 = n1 + n2 + 3
            n1 = n2
            n2 = n3
        else: 
            n3 = (n1 * n2) - 1
            n1 = n2
            n2 = n3
    print(n3)