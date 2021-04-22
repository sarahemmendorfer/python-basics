from random import randint
from time import sleep

def sorteia(lista):
    print("Sorteando os valores da lista: ")
    for cont in range(0, 5): #5 valores (0 à 4)
        n = randint(1, 10) #sorteia números
        lista.append(n) #adiciona valor na lista
        print(f'{n} ', end='')
        sleep(0.3)

def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'\nSomando os valores pares de {lista}, \ntemos uma soma de {soma}!!!')
numeros = list()
sorteia(numeros)
somaPar(numeros)
