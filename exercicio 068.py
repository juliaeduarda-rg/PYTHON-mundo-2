from random import randint
from time import sleep
resposta = ''
cont = 0
v = 0
while resposta != 'N':
    print('============================')
    print('VAMOS JOGAR IMPAR OU PAR!')
    print('============================')
    sleep(1)
    jogador = int(input('Escreva um número de 1 até 10:'))
    computador = randint(1,10)
    imparoupar = str(input('Você é impar ou par?').strip().lower())
    cimparoupar = ''
    cont += 1
    if imparoupar == 'impar':
        cimparoupar = 'par'
        print('Você escolheu {} e eu escolhi {}'.format(jogador, computador))
        sleep(1)
        if (jogador + computador) % 2 == 0:
            print('Computador ganhou')
            break
        elif (jogador + computador) % 2 != 0:
            print('Você ganhou!')
            v += 1
            resposta = str(input('Você deseja continuar? [S]x[N]').upper().strip())
    elif imparoupar == 'par':
        cimparoupar = 'impar'
        print('Você escolheu {} e eu escolhi {}'.format(jogador, computador))
        sleep(1)
        if (jogador + computador) % 2 != 0:
            print('Computador ganhou')
            break
        elif (jogador + computador) % 2 == 0:
            print('Você ganhou!')
            v += 1
            resposta = str(input('Você deseja continuar? [S]x[N]').upper().strip())
    else:
        print('Dado inválido, tente novamente.')
print(f'Em {cont} partidas você venceu {v} vezes')
