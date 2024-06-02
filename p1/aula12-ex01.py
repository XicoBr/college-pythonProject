# Escreva uma função VOGAL que receba um caractere e retorne verdadeiro se
# for uma vogal, e falso caso contrário.

def is_vogal(n):
    vogal = 'aeiouAEIOU'
    if n in vogal:
        return True
    else:
        return False


print(is_vogal('a'))
