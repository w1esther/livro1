data_nascimento = int(input('digite sua data de nascimaneto: '))

lista = []

# #esse for está lendo dígito por dígito transformado em string
for digito in str(data_nascimento):
    numero = int(digito) # transformação da string de volta para número inteiro para que ele possa voltar a ser tratado como número e possa ser realizada a soma
    lista.append(numero)

somatorio = sum(lista)
print(somatorio)

# for alternativa so usando operadores aritméticos:

data_de_nascimento = int(input('digite sua data de nascimento: '))

d1 = data_de_nascimento // 10 ** 7 % 10
d2 = data_de_nascimento // 10 ** 6 % 10
d3 = data_de_nascimento // 10 ** 5 % 10
d4 = data_de_nascimento // 10 ** 4 % 10
d5 = data_de_nascimento // 10 ** 3 % 10
d6 = data_de_nascimento // 10 ** 2 % 10
d7 = data_de_nascimento // 10 ** 1 % 10
d8 = data_de_nascimento // 10 ** 0 % 10

somatorio = d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8

print(somatorio)