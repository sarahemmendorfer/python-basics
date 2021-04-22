numero = int(input('diga um numero qualquer'))
resultado = numero%2
print('o resultado foi {}'.format(resultado))
if resultado == 0:
    print('o numero {} é par'.format(resultado))
else:
    print('o numero {} é impar'.format(resultado))