from random import randint
cont = 0
print('PAR ou ÍMPAR!!!')
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    jogada = str(input('Você quer PAR ou IMPAR: ')).upper().strip()[0]
    valor = computador + jogador
    if jogada in 'P':
        if (valor % 2) == 0:
            print('Você ganhou!!!')
            print(f'O computador jogou {computador} e você {jogador} totalizando {valor}!')
            cont += 1
        else:
            print('Você perdeu!!!')
            print(f'O computador jogou {computador} e você {jogador} totalizando {valor}!')
            break
    if jogada in 'I':
        if (valor % 2) != 0:
            print('Você ganhou!!!')
            print(f'O computador jogou {computador} e você {jogador} totalizando {valor}!')
            cont += 1
        else:
            print('Você perdeu!!!')
            print(f'O computador jogou {computador} e você {jogador} totalizando {valor}!')
            break
print(f'Você teve {cont} vitórias consecutivas.')