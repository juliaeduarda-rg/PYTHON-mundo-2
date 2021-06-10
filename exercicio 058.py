from random import randint
from time import sleep
jogador = 0
cont = 0
computador = randint(0,10)

print('====================================')
print('BEM VINDO!')
print('====================================')
sleep(1.0)
print('VAMOS JOGAR!')

while jogador != computador:
    jogador = int(input('Qual número você pensou? '))
    if jogador != computador:
        print('\033[1;31mEstá errado, tente novamente.\033[0;0m')
        cont += 1
        if jogador > computador:
            print('Meu número é menor.')
        elif jogador < computador:
            print('Meu número é maior.')
    elif jogador == computador:
        print('\033[0;32mPARABÉNS! VOCÊ VENCEU COM {} TENTATIVAS!\033[0;0m'.format(cont))
    else:
        print('ERRO')