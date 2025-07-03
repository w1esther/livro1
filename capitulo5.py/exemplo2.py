print('Digite as três notas')
n1 = int (input('N1:'))
n2 = int (input ('N2:'))
n3 = int (input('N3:'))
media = (n1+n2+n3)/3
if n3 >= 8:
    media += 1
    if media > 10:
        media = 10
print('Media:', media)