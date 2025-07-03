# calculo da soma de todos os numeros de um dado intervalo pela estrutura for

s = int(input('entre com o limite superior: '))

somatorio = 0

for n in range(1, s+1):
    somatorio += n
print(somatorio)

# calculo da soma de todos os numeros de um dado intervalo pela formula

s2 = int(input('entre com o limite superior: '))

print(n * (n+1) / 2)