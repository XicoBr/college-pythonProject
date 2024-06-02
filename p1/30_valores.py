#  Escreva um programa que leia 30 valores inteiros positivos e armazene-os em uma lista, e calcule e imprima:
#
# a) O menor valor da lista.
#
# b) A quantidade de elementos da lista que são divisíveis pelo menor valor.

from time import sleep

lista = list()
menor_valor = 0
total_div_menor_valor = 0
i = 1

while True:
    num = int(input(f'Digite o {i}o. valor: '))

    if num > 0:
        lista.append(num)
        i += 1
    else:
        print('Número inválido! Por favor, digite um número inteiro positivo.')
        sleep(2)

    if len(lista) == 30:
        break

for num in lista:
    if num == min(lista):
        menor_valor = num

for num in lista:
    if num % menor_valor == 0:
        total_div_menor_valor += 1

print('-=' * 15)
print(f'Lista de números: {lista}')
print(f'Menor número: {menor_valor}')
print(f'Total de números divididos por {menor_valor}: {total_div_menor_valor}')
