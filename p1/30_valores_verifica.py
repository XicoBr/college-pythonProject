# Escreva um programa que leia 30 números inteiros e armazene-os em uma lista A e leia também um inteiro n.
# Em seguida seu programa deve procurar o valor n em A e imprimir a posição em que este aparece.
# Se o elemento não estiver na lista,  deve-se imprimir uma mensagem indicando que o elemento não pertence a lista.

lista = []
num_check = 0
num_check_value = 0

for i in range(30):
    num = int(input(f'Digite o {i + 1}o. número inteiro: '))
    lista.append(num)

print('=-' * 15)
num_check = int(input('Digite um número para verificação: '))

for num in lista:
    if num_check == num:
        num_check_value = num
        print(f'{num_check_value} faz parte da lista.')
    else:
        print(f'{num_check_value} não faz parte da lista.')
