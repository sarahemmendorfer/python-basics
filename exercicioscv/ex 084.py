expre = str(input('Digite a expressão: '))
pilha = []
for simbolo in expre:
    if simbolo == '(':
        pilha.append('(')
    elif simbolo == ')':
        if len(pilha) > 0:
            pilha.pop() #remove o último elemento de uma lista
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão é inválida!')