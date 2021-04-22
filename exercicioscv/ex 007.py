nome = input('Qual seu nome?')
print('prazer em te conhecer {:=^20}!'.format(nome))

n1 = int(input('um valor: '))
n2 = int(input('outro valor'))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('a soma é {}, \n o produto é {} e a divisao é {:.3f}'.format(s, m, d, end=' '))
print('A divisão inteira é {} e a potencia {}'.format(di, e))