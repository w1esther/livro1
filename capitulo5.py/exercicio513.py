ano = int(input('entre com o valor de um ano e eu direi se ele é bissexto ou não: '))

if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
    print('esse ano é bissexto!')
else:
    print('esse ano não é bissexto!')