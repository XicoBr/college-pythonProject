def converte_segundos(segundos_totais):
    dias = segundos_totais // 86400  # total de segundos em um dia
    segundos_do_dia = segundos_totais % 86400  # segundos do dia restantes, que nao foram convertidos em dias
    horas = segundos_do_dia // 3600  # total de segundos de uma hora
    resto = segundos_do_dia % 3600
    minutos = resto // 60
    segundos = resto % 60
    print(f'{dias} dias, {horas} horas, {minutos} minutos, {segundos} segundos.')


converte_segundos(86400)

name = "Fulano";

_Age = 18;
print(_Age); print(name)