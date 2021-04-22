frase = str(input('Digite uma frase: ')).strip().upper() #tira espaço e torna maiúscula
palavras = frase.split() #separar a frase em palavras
junto = ''.join(palavras) #junta tudo (tira os espaços)
print('Você digitou a frase {}'.format(frase))
inverso = '' #vazio
#podia ser tbm só: (inverso = junto[::-1]) que do início (:), ao fim (:), inverte a palavra (-1)
for letra in range(len(junto) -1, -1, -1): #len(junto) -> numero de letras de junto
    inverso += junto[letra]
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')