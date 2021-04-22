lista1 = []
lista2 = []
lista3 = []
while True:
    lista1.append(int(input('Digite um número: ')))
    resp = (str(input('Deseja continuar? [S/N] ')))
    if resp in 'Nn':
        break
for i, v in enumerate(lista1):
    if v % 2 == 0:
        lista2.append(v)
    else:
        lista3.append(v)
print(f'Os números pares são: {lista2} e os número ímpares são {lista3}.')