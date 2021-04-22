frase = 'oi tudo bem'
frase[9] #identifica caracter 9 (10° caracter)
frase[9:13] #mostra caracteres do 9 ao 12
frase[9:13:2] #mostra caracteres do 9 ao 12, um sim um não
frase[:5] #mostra caracteres do inicio até o 4
frase[15:] #mostra caracteres do 15 até o final
frase[9::3] #mostra caracteres do 9 até o final, pulando 3
len(frase) #mostra qtos caracteres tem na frase (espaço conta)
frase.count('o') #mostra qtos 'o' tem na frase
frase.count('o',0,13) #mostra os 'o' de 0 à 12
frase.find('tudo') #indica onde está localizada a primeira letra (t)
'oi' in frase #diz se tem ou não 'oi' na frase
frase.replace('oi','ola') #troca oi por ola
frase.upper() #transforma em caixa alta
frase.lower() #transforma em minuscula
frase.capitalize() #só primeira letra da frase maiúscula
frase.title() #primeiras letras das palavras maiúsculas
frase.strip() #retira espaços a mais antes e depois da frase
frase.rstrip() #retira espaços à direita
frase.lstrip() #retira espaços à esquerda
frase.split() #separa cada palavra, começando a contagem do 0 em cada uma
'-'.join(frase) #adiciona '-' entre as palavras

