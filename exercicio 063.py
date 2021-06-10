cont = 0
numero = 0
print('<'*20)
print('SEQUÊNCIA DE FIBONACCI')
print('>'*20)
n = int(input('Escreva quantos termos deseja:'))
t1 = 0
t2 = 1
print( '{} - {}'.format(t1, t2), end = ' - ' )
while cont != n - 2:
    t3 = t1 + t2
    cont += 1
    print(t3, end = ' - ')
    t1 = t2
    t2 = t3
print('FIM')