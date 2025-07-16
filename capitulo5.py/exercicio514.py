valor_do_mes = int(input())

if valor_do_mes == 1:
    print('janeiro')
elif valor_do_mes == 2:
    print('fevereiro')
elif valor_do_mes == 3:
    print('março')
elif valor_do_mes == 4:
    print('abril')
elif valor_do_mes == 5:
    print('maio')
elif valor_do_mes == 6:
    print('junho')
elif valor_do_mes == 7:
    print('julho')
elif valor_do_mes == 8:
    print('agosto')
elif valor_do_mes == 9:
    print('setembro')
elif valor_do_mes == 10:
    print('outubro')
elif valor_do_mes == 11:
    print('novembro')
elif valor_do_mes == 12:
    print('dezembro')
elif 1 > valor_do_mes or valor_do_mes > 12:
    print('valor digitado não correspondente a um mês válido!')
