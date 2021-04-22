def ficha(jog='<desconhecido>', gols=0):
    print(f'O jogador {jog} fez {gols} gol(s) no campeonato.'
          f'')
nome = str(input("Nome do jogador: "))
ngol = str(input("Número de gols: "))
if ngol.isnumeric():
    ngol= int(ngol)
else:
    ngol = 0
if nome.strip() == '': #se o nome sem espaços é = vazio.
    ficha(gols=ngol) #passa só o parâmetro -> gols
else:
    ficha(nome, ngol)
