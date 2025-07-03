posicao_n = int(input('digite um número: '))

f1 = 1
f2 = 1
# f3 = f1 + f2

for n in range(3, posicao_n + 1):
    f1, f2 = f2, f1 + f2 # atribuição múltipla

if posicao_n == 1 or posicao_n == 2:
    print(f1)
else: 
    print(f2)


