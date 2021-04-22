cont = 0
while True:
    n = int(input('Digite um valor: '))
    if n < 0:
        break
    for cont in range(1, 11, 1):
        print(f'-> {n} X {cont:2} = {n * cont}')


