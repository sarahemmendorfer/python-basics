ficha = []
while True:
    nome = str(input('Nome: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2) / 2
    ficha.append([nome, [n1, n2], media])
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('.' * 100)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('¨' * 100)
for i, a in enumerate(ficha): #i: indice
    print(f'{i+1:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('.' * 100)
    opc = int(input('Você quer mostrar a nota de qual aluno? (999 cancela): '))
    if opc == 999:
        break
    elif opc <= len(ficha) - 1:
        print(f'As notas de {ficha[opc-1][0]} são {ficha[opc-1][1]}.')