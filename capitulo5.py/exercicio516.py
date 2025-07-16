idade_nadador = int(input('digite a idade do nadador: '))

if 5 <= idade_nadador <= 7:
    print('a categoria do nadador é infantil A')
elif 8 <= idade_nadador <= 10:
    print('a categoria do nadador é infantil B')
elif 11 <= idade_nadador <= 14:
    print('a categoria do nadador é juvenil A')
elif 15 <= idade_nadador <= 17:
    print('a categoria do nadador é juvenil B')
elif idade_nadador >= 18:
    print('a categoria do nadador é adultos')
elif idade_nadador < 5:
    print('idade inválida')