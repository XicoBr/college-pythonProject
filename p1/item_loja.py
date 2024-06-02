from random import randint
"""Rafaela tem uma loja de antiguidades e decidiu avaliar quanto vale o seu estoque de 1500 peças.
 Escreva um programa que receba como entrada o valor e o ano de cada item presente na loja e exiba:
a) a quantidade de itens produzidos antes de 1827
b) o valor médio dos itens
c) o ano do objeto mais valioso"""
ano_m1827 = 0  # ano abaixo de 1827
ano = []
valor = []
mais_valioso = 0  # valor do item mais valioso
ano_mais_valioso = 0  # ano de fabricação do item mais valioso
valor_total = 0  # soma o valor de todos os itens para calcular a média

for i in range(1, 1501):
    ano.append(randint(122, 2000))
    if ano[-1] < 1827:
        ano_m1827 += 1
    valor.append(randint(70, 5000))
    valor_total += valor[-1]

    if valor[-1] > mais_valioso:
        mais_valioso = valor[-1]
        ano_mais_valioso = ano[-1]
valor_medio = valor_total / 1500

print(f'Quantidade de itens produzidos antes de 1827: [{ano_m1827}]')
print(f'Valor médio dos itens: [R$ {valor_medio:.2f}]')
print(f'Valor do item mais valioso: [R$ {mais_valioso}]')
print(f'Ano em que item mais valioso foi fabricado: [{ano_mais_valioso}]')
