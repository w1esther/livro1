from math import sqrt

G = 9.80665 # m/s²

altura_torre_pisa = sqrt(2*56/G)
altura_torre_toquio = sqrt(2*333/G)

print(f'o tempo de queda de um objeto do topo da torre de pisa até o chão é de {altura_torre_pisa :.4} segundos \n\no tempo de queda de um objeto do topo da torre de tóquio até o chão é de {altura_torre_toquio :.4} segundos')