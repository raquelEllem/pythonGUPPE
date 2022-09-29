salario = float(input('Digite o salário: '))
gratificacao = (salario * 5) / 100
imposto = (salario * 7) / 100
novoSalario = salario + gratificacao - imposto
print('Salário a receber: R$ {:.2f} '.format(novoSalario))
