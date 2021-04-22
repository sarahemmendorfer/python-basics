n1 = float(input('Digite a nota 1: '))
n2 = float(input('Digite a nota 2: '))
media = (n1 + n2)/2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(n1, n2, media))
if media > 7:
    print('Você está APROVADO')
elif 7 > media >=5:
    print('O aluno está em RECUPERAÇÃO')
elif media < 5:
    print('O aluno está REPROVADO')