# Escreva uma função DIVISOR para ler dois números e retornar verdadeiro caso
# o segundo seja divisor do primeiro ou falso caso contrário

def is_second_divided(x, y):
    if y % x == 0:
        return True
    else:
        return False

print(is_second_divided(2, 6))
