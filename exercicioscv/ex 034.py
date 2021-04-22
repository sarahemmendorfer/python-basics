a = int(input('primeiro valor'))
b = int(input('segundo valor'))
c = int(input('terceiro valor'))
#verificando quem é menor
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
#verificando quem é maior
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print('o maior valor foi {}'.format(maior))
print('o menor valor foi {}'.format(menor))