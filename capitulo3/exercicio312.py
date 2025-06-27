segundos = float(input('digite os segundos: '))

horas = segundos // 60 // 60
resto = segundos % 3600
minutos = resto // 60
segundos2 = resto % 60

print(f'{horas}h{minutos}min{segundos2}s')

# página 49 constantes