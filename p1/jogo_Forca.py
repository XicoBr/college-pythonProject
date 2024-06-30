# Forca
import random
from time import sleep


palavras = ("amigo", "luzir", "risos", "pedra", "canto", "vento", "salto", "festa", "tigre", "piano")  # tupla
palavra_escolhida = random.choice(palavras)  # pega uma palavra aleatória; var é uma str
print(palavra_escolhida)
palavra_oculta = '-' * len(palavra_escolhida)  # cria uma var, com o tamanho da palavra
palavra_oculta_lista = list(palavra_oculta)  # cria uma var que é uma lista da var palavra_oculta
print(palavra_oculta_lista)
tentativas_totais = 7
letras_tentadas = list()  # cria uma var para letras utilizadas pelo player
for cont in range(7):  # player tem n tentativas p/ acertar
    print(f'{cont + 1}/{tentativas_totais} tentativa(s).')
    letra_escolhida = str(input('Digite a letra escolhida: ')).lower()
    sleep(1)
    print('-=' * 20)
    if letra_escolhida not in palavra_escolhida:
        letras_tentadas.append(letra_escolhida)
    print(f'Letras usadas: {letras_tentadas}')
    print()
    for i in range(len(palavra_escolhida)):
        if palavra_escolhida[i] == letra_escolhida:  # se a letra da palavra no indice i == a letra_escolhida
            palavra_oculta_lista[i] = letra_escolhida  # o hifen no indice i é substituido pela letra_escolhida
    print(f'Palavra: {palavra_oculta_lista}')
    print('-=' * 20)
    if '-' not in palavra_oculta_lista:
        print('Parabéns! Você ganhou!')  # encerra o prog se a palavra oculta nao tiver + hífens
        break

if '-' in palavra_oculta_lista:
    print('Que pena! Você perdeu!')
