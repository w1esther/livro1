numero = int(input())

n1 = 1
n2 = 2

for n in range(3, numero + 1):
    if n % 2 == 1: 
        n1, n2 = n2, n1 ** 2 + n2
        
    elif n % 2 == 0:
        n1, n2 = n2, n1 * 2 + n2
        

if numero == 1: 
    print(n1)
elif numero == 2:
    print(n2)
else:
    print(n2)