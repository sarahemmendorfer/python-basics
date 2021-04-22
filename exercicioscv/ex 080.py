num = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in num:
        num.append(n) #adiciona o número
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não irei adicionar...')
    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break
print('-=' * 30)
num.sort() #colaca em ordem
print(f'Você digitou os valores {num}')
