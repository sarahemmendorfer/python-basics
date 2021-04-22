def fatorial(numero, show=False):
    """
    -> Calcula o fatorial de um número.
    :param numero: Número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: Valor do Fatorial de um número.
    """
    fator = 1
    for c in range(numero, 0, -1): #de n até 0 voltando 1.
        if show:
            print(c, end='')
            if c > 1:
                print(' X ', end='')
            else:
                print(' = ', end='')
        fator *= c
    return fator

print(fatorial(5, show=True)) #mostra o cálculo
help(fatorial)