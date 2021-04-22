n = float(input('Quantos reais vc tem na carteira? R$'))
#1dolar=3,27reais
dolar = n/ 3.27
print('com R${:.2f} você pode comprar US${:.2f}'.format(n, dolar))