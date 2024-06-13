# descobrir a idade do filho mais velho de monica
# ela tem 3 filhos
# a entrada dos dados deve ser de monica e dos filhos do meio e mais novo
# saída deve ser a idade do filho + velho

def idade_mais_velho(monica, filho_meio, filho_mais_novo):
    idade_primogenito = monica - (filho_meio + filho_mais_novo)
    print(idade_primogenito)


idade_mais_velho(52, 18, 14)
