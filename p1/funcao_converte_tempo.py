def converte_tempo_segundos(segundos_totais):
    horas = segundos_totais // 3600  # 3600s, uma vez que 1 hora tem 3600 segundos
    resto = segundos_totais % 3600
    minutos = resto // 60
    segundos = resto % 60

    print(f'{horas:02d}:{minutos:02d}:{segundos:02d}')


def converte_tempo_minutos(minutos_totais):
    converte_tempo_segundos(minutos_totais * 60)


def converte_tempo(total, unidade):
    if unidade == 'segundos':
        converte_tempo_segundos(total)
    elif unidade == 'minutos':
        converte_tempo_minutos(total)
    else:
        print('Unidade inválida!')


converte_tempo(65, 'segundos')
