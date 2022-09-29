from datetime import datetime

idade = int(input('Informe  a idade: '))
data_atual = datetime.now()
print('Ano de nascimento {}'.format(data_atual.year - idade))
