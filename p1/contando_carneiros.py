# If you can't sleep, just count sheep!!

def count_sheep(n):  # lembrar que, em funções, não é bom printar a saída de uma ação, e sim o seu retorno
    if n == 0:
        return ''

    resultado = ''  # começa vazio para ser incrementado na iteração do 'for' abaixo
    for i in range(1, n + 1):
        resultado += f"{i} sheep" if i == 1 else f"{i} sheeps"  # otimização de código; condicionais na mesma linha
        resultado += '...'
    return resultado.strip()  # remove os espaços vazios entre as palavras


print(count_sheep(0))

# Segundo Exemplo

# join concatena todos os elementos da lista sem espaços entre eles; a lista abaixo é compreendida pelo uso das
# tuplas []
# for i in range itera sobre cada elemento da lista
# se n = 2, temos: ['1 sheep...', '2 sheep...']
# se n = 0, produz uma lista vazia [], e o ''.join([]) resulta em uma string vazia ""

"""def count_sheep(n):  
    return ''.join([f"{i+1} sheep..." for i in range(n)])


print(count_sheep(0))"""
