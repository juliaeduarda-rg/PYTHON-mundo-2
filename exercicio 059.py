n1 = int(input('Escreva um valor:'))
n2 = int(input('Escreva um outro valor:'))
escolha = 0

while escolha != 5:
    escolha = int(input('''
    Escolha uma opção:
    [1]Soma
    [2]Multiplica
    [3]Maior
    [4]Novos números
    [5]Sair do programa'''))
    print('      ')
    if escolha == 1:
        print('{} + {} = {}'.format(n1, n2, n1+n2))
    elif escolha == 2:
        print('{} x {} = {}'.format(n1, n2, n1 * n2))
    elif escolha == 3:
        if n1 > n2:
            print('{} é maior que {}'.format(n1, n2))
        else:
            print('{} é maior que {}'.format(n2, n1))
    elif escolha == 4:
        n1 = int(input('Escreva um valor:'))
        n2 = int(input('Escreva um outro valor:'))