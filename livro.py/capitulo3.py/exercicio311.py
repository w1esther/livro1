from math import sqrt

a = float(input('digite o valor da variável A: '))
b = float(input('digite o valor da variável B: '))
c = float(input('digite o valor da variável C: '))

delta = (b**2) - (4 * a * c)

x1 = (-b + (sqrt(delta))) / (2 * a)
x2 = (-b - (sqrt(delta))) / (2 * a)

print(f'as raízes da equação são: {x1} e {x2}')