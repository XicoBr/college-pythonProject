#  Entrada
# A entrada contém duas strings, A e B, a direção para onde seu amigo está virado originalmente
# e a direção do oásis, respectivamente.
#
# Saída
# Seu programa deve produzir uma única linha, contendo um único inteiro, o menor ângulo que seu amigo deve virar
# para continuar na direção correta para o oásis.
# Restrições
# Os valores possíveis para A e B são {norte, leste, oeste, sul}.

direcao = {
    'norte': 0,
    'leste': 90,
    'sul': 180,
    'oeste': 270
}
direcao_amigo = str(input('Digite a direção do amigo [norte/leste/sul/oeste]: ')).lower()
angulo_amigo = direcao[direcao_amigo]
direcao_oasis = str(input('Digite a direção do oasis [norte/leste/sul/oeste]: ')).lower()
angulo_oasis = direcao[direcao_oasis]
diferenca = abs(angulo_amigo - angulo_oasis)

menor_diferenca = min(diferenca, 360 - diferenca)
print(menor_diferenca)
