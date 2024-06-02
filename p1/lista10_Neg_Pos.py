# Faça um programa que preencha uma lista com 10 números,
# calcule e mostre a quantidade de números negativos e a soma dos números positivos dessa lista.

lista = list()
total_negativos = 0
soma_positivos = 0
for i in range(3):
    num = float(input(f'Digite o {i + 1}o. número: '))
    lista.append(num)
for num in lista:
    if num < 0:
        total_negativos += 1
    else:
        soma_positivos += num
print('-=' * 15)
print(f'Listagem de números: {lista}')
print(f'Total de números negativos: {total_negativos}')
print(f'Soma dos números positivos: {soma_positivos}')
