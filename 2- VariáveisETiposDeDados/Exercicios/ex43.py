valor = float(input('Digite o valor do produto: '))
desconto = valor - ((valor * 10) / 100)
parcela = valor / 3
comissaoAVista = (desconto * 5) / 100
comissaoParcela = (valor * 5) / 100
print('Desconto de 10%: R$ {:.2f} '.format(desconto))
print('Parcela 3x sem juros: R$ {:.2f} '.format(parcela))
print('Comissão (5%) para venda à vista: R$ {:.2f} '.format(comissaoAVista))
print('Comissão (5%) para venda parcelada: R$ {:.2f} '.format(comissaoParcela))