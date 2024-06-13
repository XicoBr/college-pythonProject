# dada uma sequência de números informada pelo usuario, adicioná-los em uma lista sempre que for um número diferente
# de zero. Se zero, remover da lista

def zero_cancela(numeros):
    pilha = []
    for numero in numeros:
        if numero != 0:
            pilha.append(numero)
        else:
            pilha.pop()

    print(pilha)
    return sum(pilha)


tot_numeros = int(input('Informe o total de números: '))
numeros_lista = []
contador = 1


for _ in range(tot_numeros):  # o underscore é comumente usado como uma convenção para indicar que o valor da
    # variável não será utilizado
    numeros_lista.append(int(input(f'Digite o {contador}o. número: ')))
    contador += 1

resultado = zero_cancela(numeros_lista)

print(resultado)
