listagem = ('lapis', 2,
            'borracha', 3,
            'caderno', 13.5,
            'mochila', 100,
            'caneta', 2.50,
            'regra', 3.50)
print('-' * 30)
print('LISTAGEM DE PREÇOS: ^40') #40 espaços centralizado
print('-' * 30)
for pos in range(0, len(listagem)): #até o tamanho da lista
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='') #mostra com 30 caracteres (pontos alinhados à esquerda
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('-' * 30)