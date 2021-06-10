from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
jogador = int(input('''Escolha uma opção:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA\nVocê escolhe:'''))
print('Você jogou {}.\nE eu joguei {}.'.format(itens[jogador], itens[computador]))
if computador == jogador:
    print('EMPATE')
elif computador == 0 and jogador == 2 or computador == 1 and jogador == 0 or computador == 2 and jogador == 1:
    print('Eu ganhei!')
elif jogador == 0 and computador == 2 or jogador == 1 and computador == 0 or jogador == 2 and computador == 1:
    print('Você venceu!')
else:
    print('Ação inválida!')