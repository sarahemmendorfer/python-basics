resposta = 'S'
media = soma = quantidade = maior = menor = 0
while resposta in 'Ss':
    n = int(input('Digite um número: '))
    soma += n
    quantidade += 1
    if quantidade == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
    resposta = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
media = soma / quantidade
print('Você digitou {} números e a média foi {}.'.format(quantidade, soma))
print('O menor número foi {} e o maior número foi {}.'.format(menor, maior))
