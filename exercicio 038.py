n1 = int(input('Escreva um número: '))
n2 = int(input('Escreva outro número: '))
if n1 == n2:
    print('Não existe maior, ambos tem o mesmo valor.')
elif n1>n2:
    print('O número {} é maior que o número {}.\nO primeiro valor é maior.'.format(n1, n2))
elif n2>n1:
    print('O número {} é maior que o número {}.\nO segundo valor é maior'.format(n2, n1))