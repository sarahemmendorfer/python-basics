def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('ERRO: Por favor, digite um número inteiro válido')
            continue #joga de novo pro while
        except (KeyboardInterrupt):
            print('Entrada de dados interrompida pelo usuário')
            return 0
        else:
            return n

def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('ERRO: Por favor, digite um número inteiro válido')
            continue #joga de novo pro while
        except (KeyboardInterrupt):
            print('Entrada de dados interrompida pelo usuário')
            return 0
        else:
            return n
n1 = leiaInt('Digite um valor inteiro: ')
n2 = leiaFloat('Digite um valor Real: ')
print(f'O valor inteiro digitado foi {n1} e o Real foi {n2}')