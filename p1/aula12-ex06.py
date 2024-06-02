# 6.  O estacionamento do Shopping Total era gratuito até o mês passado, mas agora
# passou a ser pago. Cada veículo deverá pagar uma taxa de R$ 3,00 por até 5
# horas de estacionamento, e R$ 2,00 por cada hora ou fração de hora (Ex: 15
# minutos, 32 minutos) a mais. Se o veículo for uma moto, esses valores caem
# pela metade.
# Escreva a função calculaEstacionamento que receba o tipo de veículo e seu
# tempo de permanência (total de horas e total de minutos) e retorne o valor a ser
# pago.


def calcula_estacionamento(veiculo, horas, minutos):
    horas_excedentes = 0
    total_pagar = 0
    if veiculo.lower() == 'carro':
        taxa_hora_fixa = 3
        taxa_hora_extra = 2
        print('Veículo: Carro')
        if horas <= 5 and minutos == 0:
            print(f'Valor a pagar: R${taxa_hora_fixa}')
        else:
            horas_excedentes = horas - 5
            if minutos > 0:
                horas_excedentes += 1
                print(f'Valor a pagar: R${taxa_hora_fixa + (horas_excedentes * taxa_hora_extra)}')

    elif veiculo.lower() == 'moto':
        taxa_hora_fixa = 1.50
        taxa_hora_extra = 1.00
        print('Veículo: Moto')
        if horas <= 5:
            print(f'Valor a pagar: R${taxa_hora_fixa}')
        else:
            horas_excedentes = horas - 5
            if minutos > 0:
                horas_excedentes += 1
                print(f'Valor a pagar: R${taxa_hora_fixa + (horas_excedentes * taxa_hora_extra)}')
            else:
                print(f'Valor a pagar: R${taxa_hora_fixa + (horas_excedentes * taxa_hora_extra)}')


calcula_estacionamento('moto', 7, 0)


