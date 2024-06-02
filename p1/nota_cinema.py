from random import randint
'''Escreva um programa que receba como entrada a idade e a opinião (código) de 500 espectadores, calcule e exiba:

a) a média de idade das pessoas que responderam bom

b) a quantidade de pessoas que responderam ruim ou regular

c) a quantidade de pessoas acima de 30 anos que responderam excelente

d) a idade da pessoa mais velha que respondeu o questionário'''
idade = list()
notas = list()
idade_4 = 0  # idade de pessoas que deram nota 4
tot_pessoas4 = 0  # total de pessoas que deram nota 4
idade_1_2 = 0  # idade de pessoas que deram nota 1 ou 2
tot_pessoas_1_2 = 0  # total de pessoas que deram nota 1 ou 2
mais_velho = 0  # autoexplicativo
idade_mais_30 = 0  # pessoas com mais de 30 anos que avaliaram o filme

for i in range(1, 501):
    idade.append(randint(18, 75))
    if idade[-1] > mais_velho:
        mais_velho = idade[-1]
    notas.append(randint(1, 4))
    if notas[-1] == 4:  # se a última nota adicionada for igual a 4
        idade_4 += idade[-1]  # adiciona a idade da ultima pessoa à variável
        tot_pessoas4 += 1
        if idade[-1] > 30:
            idade_mais_30 += 1

    elif notas[-1] == 1 or notas[-1] == 2:
        idade_1_2 += idade[-1]
        tot_pessoas_1_2 += 1

if tot_pessoas4 > 0:
    media_idade4 = idade_4 / tot_pessoas4  # média da idade das pessoas que deram nota 4
    print(f'Total de pessoas que deram nota 4: [{tot_pessoas4}] pessoa(s).')
    print(f'Média de idade: [{media_idade4:.1f}] anos.')
    if idade_mais_30 > 0:
        print(f'Quantidade de pessoas acima de 30 anos e que deram nota 4: [{idade_mais_30}].')

print('-=' * 30)

if tot_pessoas_1_2 > 0:
    media_idade_1_2 = idade_1_2 / tot_pessoas_1_2
    print(f'Total de pessoas que deram nota 1 ou 2: [{tot_pessoas_1_2}]')
    print(f'Média de idade: [{media_idade_1_2:.1f}] anos.')

print('-=' * 30)
print(f'Idade da pessoa mais velha a avaliar o filme: [{mais_velho}] anos.')