def notas(*n, situacao=False):
    """
    --> Analisando as notas dos alunos:
    :param n: notas dos alunos
    :param situacao: valor que indica se deve-se adicionar a situação
    :return: retorna a situação do aluno
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n)/len(n)
    if situacao: #se situação for verdadeira
        if r['média'] >= 7:
            r['situação'] = 'BOA'
        elif r['média'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r
resp = notas(5, 6, 7, situacao=True)
print(resp)
help(notas)