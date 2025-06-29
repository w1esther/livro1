numero = int(input())

n1 = 2
n2 = 3

# o laço só é executado se numero > 2
for n in range(3, numero + 1): 
    n1, n2 = n2, n1 * n2

if numero == 1:
    print(n1)
elif numero == 2:
    print(n2)
else: 
    print(n2)