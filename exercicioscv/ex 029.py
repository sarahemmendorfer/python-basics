from random import randint
from time import sleep
computador = randint(0,5) #faz computador pensar
print('-=-' * 20)
print('vou pensar num numero, tente adivinhar')
print('-=-' * 20)
jogador = int(input('em que numero pensei?'))
print('processando...')
sleep(3)
if jogador == computador:
     print('parabéns')
else:
      print('ganhei! eu pensei no numero {} e nao no {}!'.format(computador, jogador))