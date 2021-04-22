times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio',
         'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense',
         'Atlético', 'Botafogo', 'Atlético-PR', 'Bahia',
         'São Paulo', 'Fluminense', 'Sport Recife',
         'EC Vitória', 'Coritiba', 'Avaí', 'Ponte Preta',
         'Atlético-GO')
print('-=' * 15)
print(f'Lista de times: {times}')
print('-=' * 15)
print(f'Os cinco primeiros são: {times[0:5]}')
print('-=' * 15)
print(f'Os quatro últimos colocados são: {times[-4:]}')
print('-=' * 15)
print(f'Times em ordem alfabética: {sorted(times)}') #ordem alfabética
print('-=' * 15)
print(f'A Chapecoense está na {times.index("Chapecoense")+1} posicão! ') #index busca onde esta a Chapecoense
print('-=' * 15)
