from datetime import date
ano = int(input('Que ano quer analizar? Coloque 0 para analizar o ano atual'))
if ano == 0:
    ano = date.today().year
if ano %4 == 0 and ano%100 != 0 or ano %400 == 0:
    print('o ano {} é bissexto'.format(ano))
else:
    print('o ano {} não é bissexto'.format(ano))