n1 = float(input('digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))
m=(n1+n2)/2
print('A sua media foi {:.1f}'.format(m))
if m >= 6.0:
    print('Sua média foi boa!')
else:
    print('sua média foi ruim!')