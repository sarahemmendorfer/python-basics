from time import sleep

def maior(* num): #vários parâmetros
    cont = maior = 0
    print('\nAnalisando os valores passados: ')
    for valor in num:
        print(f'{valor} ', end='')
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'\nForam informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')

maior(2, 5, 7, 8, 11)