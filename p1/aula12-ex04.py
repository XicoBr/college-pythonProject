# Escreva um programa para ler 50 números e exibir a quantidade de números
# que são múltiplos de 3 e divisores de 8 usando as funções MULT3 e DIVISOR
# criadas anteriormente.
from random import randint
lista = []

def is_mult3_and_divisor():
    mult3_divided8 = 0
    for i in range(0, 50):
        lista.append(randint(1, 100))
        if lista[i] % 3 == 0 and lista[i] % 8 == 0:
            mult3_divided8 += 1

    print(f'Quantia de números dididos por 3 e múltiplos de 8: [{mult3_divided8}]')


is_mult3_and_divisor()
