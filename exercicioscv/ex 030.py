velocidade = float(input('qual a velocidade do carro?'))
if velocidade > 80:
    print('Multado!')
    multa = (velocidade-80) * 7
    print('Você deve pagar uma multa de R${:.2f}'.format(multa))
print('Tenha um bom dia!')