escolha = 'S'
while escolha == 'S':
    n = int(input('Escreva um número:'))
    r = int(input('Razão:'))
    d = n + (11 - 1) * r
    escolha = ' '
    while n < d:
        print('{}'.format(n), end='-')
        n = n + r
    else:
        escolha = input('\nDeseja continuar?[S]X[N]\n').upper()
