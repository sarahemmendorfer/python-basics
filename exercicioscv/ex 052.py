soma = 0
for c in range(1, 7):
    num = int(input('Digite o {}° número inteiro: '.format(c)))
    if num % 2 == 0:
        soma += num
print('A soma dos número pares é {}!'.format(soma))
