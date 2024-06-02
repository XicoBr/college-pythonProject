""""5. As vendas de abadás de um bloco para o sábado de carnaval já são um grande sucesso. A estratégia do bloco foi
colocar 100 comissários nas ruas para vender as fantasias, cada uma custando R$ 80. Para cada abadá vendido,
o comissário recebe um percentual de 7%, e caso venda mais de 50 fantasias, recebe um bônus de R$ 70. Supondo que o
bloco disponha de 3000 abadás para vender, escreva um programa que receba como entrada a quantidade de fantasias
vendidas por cada comissário e, usando as funções calculaComissao e calculaBonus, também escritas por você,
exiba o valor pago pelo bloco a cada um deles, e também a quantidade de abadas ainda disponíveis.
Função calculaComissao: recebe a quantidade de abadás vendidos e retorna a comissão correspondente.
Função calculaBonus: recebe a quantidade de abadás vendidos e retorna o valor do bônus."""

abadas_vendidos = []
i = 0
abadas_disponiveis = 3000
calcula_comissao = []
preco_abada = 80
comissao = []
while i < 10:
    abadas_vendidos.append(int(input(f'Digite o número vendido pelo Comissário [{i + 1}]: ')))
    abadas_disponiveis -= abadas_vendidos[i]
    if abadas_vendidos[i] < 50:
        calcula_comissao = (abadas_vendidos[i] * preco_abada) * 0.07
        comissao.append(calcula_comissao)

    elif abadas_vendidos[i] >= 50:
        calcula_comissao = ((abadas_vendidos[i] * preco_abada) * 0.07) + 70
        comissao.append(calcula_comissao)
    i += 1

for comissario, vendidos in enumerate(abadas_vendidos):  #A função enumerate é uma função embutida no Python que adiciona um contador (índice) a um iterável (como uma lista). O resultado é um objeto que produz pares contendo um índice e o valor correspondente do iterável.
    print(f"Comissário [{comissario + 1}] vendeu {vendidos} abadás e sua comissão é: R${comissao[comissario]:.2f}")
