primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
décimo = primeiro + (10 - 1) * razão #fórmula do enésimo termo de uma PA
for c in range(primeiro, décimo + razão, razão):
    print('{}'.format(c), end=' -> ')
print('TERMINOOOU!!!')