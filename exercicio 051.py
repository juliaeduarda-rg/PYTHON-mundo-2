n = int(input('Escreva um número:'))
r = int(input('Razão:'))
d = n +(11 - 1) * r
for PA in range(n, d, r):
    print('{}'.format(PA), end = '-')