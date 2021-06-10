n2 = 0
for i in range (0, 6):
    n1 = int(input('Escreva um número par:'))
    n2 += n1
if n1 % 2 != 0:
    print('Você escreveu um número impar. Opção inválida!')
elif n1 % 2 == 0:
    print('A soma é {}'.format(n2))
else:
    print('Não sei oq tu fez, mas não vai rolar.')