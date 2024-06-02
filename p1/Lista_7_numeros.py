#  Escreva um programa que lê 7 valores inteiros, armazena-os em uma lista e, em seguida,
#  mostra os valores lidos em  ordem inversa à leitura
from time import sleep
numeros = []
for i in range(7):
    while True:  # try e except são blocos de exceções
        try:  # converte o valor inserido para número inteiro
            num = int(input(f'Digite o {i + 1}o. número inteiro: '))
            numeros.append(num)
            break  # interrompe o laço de repetição se o valor não puder ser convertido para número inteiro
        except ValueError:  # executado se ocorrer um erro do tipo ValueError, quando a conversão p/ inteiro falha
            print('=-' * 21)
            print(f'Número/cactere inválido! Tente novamente.')
            print('=-' * 21)
            sleep(1.5)
numeros.reverse()
print(f'Lista em ordem inversa: {numeros}')
