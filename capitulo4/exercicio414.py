lista =[]

for n in range(1, 65):
    graos = 2 ** (n - 1) # formula de uma pg
    lista.append(graos)

somatorio = sum(lista)

print(f'a quantidade necessária de grãos de arroz pra efetuar o pagamente é de {somatorio} grãos')
