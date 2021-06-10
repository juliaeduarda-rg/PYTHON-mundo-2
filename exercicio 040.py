from time import sleep
n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))
M = (n1 + n2 / 2)
print('Sua média foi {}'.format(M))
sleep(2)
if M<5.0:
    print('Você está...')
    sleep(2)
    print('\033[1;31mREPROVADO\033[1;31m')
elif 6.9>M>5.0:
    print('Você está...')
    sleep(2)
    print('\033[1;34mEM RECUPERAÇÃO\033[1;34m')
elif M>=7.0:
    print('Você está...')
    sleep(2)
    print('\033[0;32mAPROVADO\033[0;32m')