from math import pow
num1 = float(input('Digite o 1º número: '))
num2 = float(input('Digite o 2º número: '))
num3 = float(input('Digite o 3º número: '))
print('Resultado de {}² + {}² + {}² = {}'.format(num1, num2, num3, pow(num1, 2) + pow(num2, 2) + pow(num3, 2)))
