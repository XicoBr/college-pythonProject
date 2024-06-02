def num_primo(numero):
    primo_check = True
    for i in range(2, numero):
        if numero % i == 0:
            primo_check = False
            break
        return primo_check


num = int(input('Digite um número: '))
if num_primo(num):
    print('É primo')
else:
    print('Não é primo')
