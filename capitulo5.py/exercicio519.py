moeda = str(input())
valor_em_reais = float(input())

if moeda == 'e' and valor_em_reais > -1:
    valor1 = valor_em_reais * 0.31
    print(valor1)
elif moeda == 'd' and valor_em_reais > -1:
    valor2 = valor_em_reais * 0.42
    print(valor2)
elif moeda == 'm' and valor_em_reais > -1:
    valor3 = valor_em_reais * 5.55
    print(valor3)
elif moeda == 'a' and valor_em_reais > -1:
    valor4 = valor_em_reais * 2.84
    print(valor4)
elif moeda == 'l' and valor_em_reais > -1:
    valor5 = valor_em_reais * 0.36
    print(valor5)
elif valor_em_reais < 0:
    print('quantidade inválida')
elif moeda == 'b' or moeda == 'c' or moeda == 'f' or moeda == 'g' or moeda == 'h' or moeda == 'i' or moeda == 'j' or moeda == 'k' or moeda == 'n' or moeda == 'o' or moeda == 'p' or moeda == 'q' or moeda == 'r' or moeda == 's' or moeda == 't' or moeda == 'u' or moeda == 'v' or moeda == 'w' or moeda == 'x' or moeda == 'y' or moeda == 'z':
    print('moeda inválida')