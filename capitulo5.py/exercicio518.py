peso = float(input('digite o seu peso em kg: '))
altura = float(input('digite sua altura em metros: '))

imc = peso / (altura ** 2)

if imc < 18.5:
    print(f'{imc}, adulto com baixo peso')
elif 18.5 <= imc < 25:
    print(f'{imc}, adulto com peso adequado')
elif 25 <= imc < 30:
    print(f'{imc}, adulto com sobrepeso')
elif imc >= 30:
    print(f'{imc}, adulto com obesidade')