#  Para elaborar um código em Python que determina em qual grupo um participante
#  será colocado com base nos resultados dos jogos,
#  você precisará seguir as seguintes instruções

# Ler seis linhas de entrada, cada uma contendo 'V' (vitória) ou 'P' (perda).
# Contar o número de vitórias.
# Determinar o grupo com base no número de vitórias.
# Imprimir o número do grupo correspondente ou -1 se o participante não vencer nenhum jogo.


jogador = str(input('Digite o número do jogador :'))
vitorias = 0
for i in range(1, 7):

    partida = str(input(f'Partida {i} [v/d]: ')).lower()
    if partida == 'vitoria' or partida == 'v':
        vitorias += 1

if vitorias >= 5:
    print(f'Jogador {jogador} ---- Grupo 1')
elif 3 <= vitorias <= 4:
    print(f'Jogador {jogador} ---- Grupo 2')
elif 1 <= vitorias <= 2:
    print(f'Jogador {jogador} ---- Grupo 3')
elif vitorias == 0:
    print(f'Jogador {jogador} está desclassificado.')
