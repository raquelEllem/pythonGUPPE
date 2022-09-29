valor = float(input('Digite o valor do produto: '))
novoValor = (valor - (valor * 12) / 100)
print('Novo valor com desconto de 12%: R$ {:.2f} '.format(novoValor))