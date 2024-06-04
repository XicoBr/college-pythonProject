# mod 2: condicionais (if, else, elif, switch)
# -crie um algoritmo q verifique se o usuário é maior de idade ou não (extra: xingar o usuário caso ele seja de menor)
# -usando elif faça com que o algoritmo também verifique se o usuário tem mais de 60 anos
# -usando o switch, crie um algoritmo que verifique se usuário tem:
# <10,20,50,60 ou 100+ anos de idade (extra: xingar o user)

# mod 3: Loops (while e for)
# -usando WHILE crie um algoritmo que printa "faz o L" na tela 100 vezes

# mod 4: listas tuplas e dicionários
# -usando FOR crie um algoritmo que itere por uma lista ou tupla e printe seus itens

# mod 5: funções
# - usando DEF crie uma função que recebe 2 argumentos e some ambos, e utilize a função

# mod 6: usando bibliotecas externas
# -faça oq raul me proibiu de fazer (importe a biblioteca math e use a função sqrt para calcular a raiz quadrada)
#
# -crie um algoritmo que dada uma lista 'alunos' e outra 'notas' crie um dicionário que receba
# as 2 listas como itens e chaves
# e mostre qual aluno tem a maior nota

alunos = ['Ana', 'Beto', 'Carla']
notas = [7.0, 5.5, 8.0]
dic_final = {}
val = 0
maior_nota = 0e
for aluno, nota in zip(alunos, notas):  # zip agrupa em dupla 1 elemento de cada lista
    dic_final[aluno] = nota  # o índice 'aluno' recebe o valor 'nota'
    if nota > maior_nota:
        maior_nota = nota

print(dic_final.keys())  # mostra as chaves de um dicionario. Lembrar que chave está para índice
print(dic_final.values())  # mostra os valores de cada elemento
print(dic_final.items())  # mostra as chaves e os valores de cada elemento
print(maior_nota)
