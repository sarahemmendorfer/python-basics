from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''\033[1;31mSuas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA\033[m''')
jogador = int(input('Qual é a sua jogada? '))
if jogador > 3:
    print('Jogada INVÁLIDA!')
    exit()
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
print('-=' *10)
print('O computador escolheu {}'.format(itens[computador])) #item na posição computador
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' *10)

if computador == 0:
    if jogador == 0:
        print('EMPATOU!')
    elif jogador == 1:
        print('GANHOU!')
    elif jogador == 2:
        print('PERDEU!')
elif computador == 1:
        if jogador == 0:
            print('PERDEU!')
        elif jogador == 1:
            print('EMPATOU!')
        elif jogador == 2:
            print('GANHOU!')
elif computador == 3:
        if jogador == 0:
            print('GANHOU!')
        elif jogador == 1:
            print('PERDEU!')
        elif jogador == 2:
            print('EMPATOU!')
