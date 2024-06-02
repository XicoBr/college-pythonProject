#  Escreva um programa que leia 20 notas e armazene-as em uma lista chamada notas.
#  Em seguida calcule e imprima a média das  notas, as notas que estão acima da média e a maior nota digitada.

notas = []  # ou list()
soma_notas = 0
maior_nota = 0
media = 0
acima_media = []
for i in range(20):
    nota = float(input(f'Digite a {i + 1}a. nota: '))
    notas.append(nota)
    soma_notas += nota

    if nota > maior_nota:
        maior_nota = nota
media = soma_notas / len(notas)

for cont in range(20):
    if notas[cont] > media:
        acima_media.append(notas[cont])
print('-=' * 10)
print(f'Média das notas: {media}')
print(f'Notas acima da média: {acima_media}')
print(f'Maior nota: {maior_nota}')
