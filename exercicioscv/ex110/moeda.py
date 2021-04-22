def aumentar(preço = 0, taxa = 0, formato=False):
    res = preço + (preço * taxa/100)
    return res if format is False else moeda(res)

def diminuir(preço = 0, taxa = 0, formato=False):
    res = preço - (preço * taxa / 100)
    return res if format is False else moeda(res)

def dobro(preço = 0, formato=False):
    res = preço * 2
    return res if format is False else moeda(res)

def metade(preço = 0, formato=False):
    res = preço / 2
    return res if not format else moeda(res)


def moeda(preço = 0, moeda = 'R$'):
    return f'{moeda}{preço:>.2f}'.replace('.',',') #substitui ponto por vírgula

def resumo(preço=0, taxaaum=10, taxared=5):
    print('-' * 40)
    print('RERSUMO DO VALOR'.center(40))
    print('-' * 40)
    print(f'Preço analisado: \t\t\t{moeda(preço)}') #tabulação
    print(f'Dobro do preço: \t\t\t{dobro(preço, True)}')
    print(f'Metade do preço: \t\t\t{metade(preço, True)}')
    print(f'Com {taxaaum}% de aumento: \t\t{aumentar(preço, taxaaum, True)}')
    print(f'Com {taxared}% de redução: \t\t\t{diminuir(preço, taxared, True)}')
    print('-' * 40)
