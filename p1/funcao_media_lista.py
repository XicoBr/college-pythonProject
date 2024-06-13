# programa deve retornar a media dos numeros de uma lista

def find_average(numbers):
    if not numbers:
        return 0
    soma = sum(numbers)
    media = soma / len(numbers)
    return media


numeros = []
print(find_average(numeros))
