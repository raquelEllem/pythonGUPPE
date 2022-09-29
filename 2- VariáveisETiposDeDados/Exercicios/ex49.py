from datetime import datetime
from datetime import timedelta

inicio = input('Informe  o horário de início, seguindo o formato -> HH:MM:SS: ')
inicio = datetime.strptime(inicio, '%H:%M:%S')
segundos = int(input('Informe a duração do experimento em segundos: '))
final = inicio + timedelta(seconds=segundos)
print('O experiemento terminou {}'.format(final.time()))