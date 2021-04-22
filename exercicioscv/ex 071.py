total = totmil = menor = cont = 0
barato = ''
while True:
    produto = str(input('Nome do produto: '))
    preço = float(input('Preço: R$ '))
    cont += 1
    total += preço
    if preço > 1000:
        totmil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA ')) #centralizado em 40 caracteres
print(f'O total da compra foi {total:.2f} reais.')
print(f'Temos {totmil} produtos que custaram mais de 1000 reais.')
print(f'O produto mais barato foi o/a {produto} e custou {menor:.2f} reais.')

