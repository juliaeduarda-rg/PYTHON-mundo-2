num = int(input('digite um numero:'))
d = 0
for c in range(1, num +1):
    if num % c == 0:
        print('\033[34m')
        d += 1
    else:
        print('\033[m')
    print('{}'.format(c))
print('O número {} foi divisivel {} vezes.'.format(num, d))
if d == 2:
    print('Seu número é um número primo.')
else:
    print('Seu número não é um número primo.')