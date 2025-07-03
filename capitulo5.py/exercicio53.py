qualidade = float(input())
preco = float(input())
prazo = float(input())

if qualidade < 7:
    print('a nota geral é 0')
elif qualidade >= 7 and preco >= 7:
    nota_geral = (preco + prazo + qualidade) / 3
    print(f'a nota geral é: {nota_geral}')
elif qualidade >= 7 and preco < 7:
    nota_geral = (qualidade + 2 * preco + prazo) / 4
    print(f'a nota geral é: {nota_geral}')

# página 76