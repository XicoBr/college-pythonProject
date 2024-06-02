# Escreva uma função MULT3 que receba um número e retorne verdadeiro se ele
# for múltiplo de 3, e falso caso contrário

def mult_3(n):
    if n % 3 == 0:
        return True
    else:
        return False


print(mult_3(12))
