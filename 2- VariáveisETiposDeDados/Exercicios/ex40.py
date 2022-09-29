dias = int(input('Digite o número de dias trabalhados: '))
salario = 30 * dias
imposto = (salario * 8) / 100
print('Salário (- imposto de 8%): R$ {:.2f} '.format(salario - imposto))
