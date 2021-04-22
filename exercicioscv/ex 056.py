from datetime import date
atual = date.today().year
totalmaior = 0
totalmenor = 0
for pessoa in range(1, 8):
    nascimento = int(input('Em que ano a {}° pessoa nasceu?'.format(pessoa)))
    idade = atual - nascimento
    if idade >= 21:
        totalmaior += 1
    else:
        totalmenor += 1
print('Tivemos {} pessoas maiores de idade e {} pessoas menores de idade!'.format(totalmaior, totalmenor))