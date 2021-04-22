distancia = float(input('Qual é a  distância da sua viagem?'))
print('vc esta prestes a começar uma viagem de {}km.'.format(distancia))
'''if distancia <=200:
    preço = distancia*0.50
else:
    preço = distancia*0.45'''
preço = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('E o preço da sua passagem é R${:.2f}'.format(preço))