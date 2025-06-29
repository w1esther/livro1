numero = int(input())

n1 = 0
n2 = 1
n3 = 1

for n in range(4, numero + 1):
    n1, n2, n3 = n2, n3, n1 + n2 + n3
        
    if n3 % 5 == 0: #atenção
        n3= n3 * 2
if numero == 1:
    print(n1)
elif numero == 2:
    print(n2)
elif numero == 3:
    print(n3)
else: 
    print(n3)