lista = list()  # lista vazia, tbm pode ser lista = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[len(lista)-1]: #ou lista[-1], pega o ultimo elemento (se n for maior que o último elemento)
        lista.append(n)
        print('Adicionado no final da lista!')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n) #insere valor n na posição pos
                print(f'Adicionado na posição {pos}!')
                break
            pos += 1
print('-=' * 30)
print(f'Os valores digitados em ordem foram {lista}')