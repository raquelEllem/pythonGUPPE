valor = float(input('Digite o valor da hora de trabalho: '))
horas = float(input('Digite a quantidade de horas trabalhadas: '))
salario = valor * horas
print('Salário (+ 10%): R$ {:.2f} '.format(salario + (salario * 10) / 100))
