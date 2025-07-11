lado1 = int(input('entre com o valor do 1º lado:'))
lado2 = int(input('entre com o valor do 2º lado: '))
lado3 = int(input('entre com o valor do 3º lado: '))

if lado1 + lado2 <= lado3 or lado1 + lado3 <= lado2 or lado2 + lado3 <= lado1:
    print('não, esses valores não podem formar um triângulo')
else:
    print('sim, esses valores podem formar um triângulo')