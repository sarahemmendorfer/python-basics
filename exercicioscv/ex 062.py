#from math import factorial
n = int(input('Digite um número para calcular o seu fatorial: '))
#f = factorial(n)
c = n
f = 1
print('Calculando {}! =')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('O fatorial de {} é {}. '.format(n, f))