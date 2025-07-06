for n in range (2, 10001):
    divisores = []
    for i in range (1, n):
        if n % i == 0:
            divisores.append(i)
    if sum(divisores) == n:
        print(f'{n} é um número perfeito')
    