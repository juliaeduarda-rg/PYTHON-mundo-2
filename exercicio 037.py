N = int(input('Escreva o número que deseja tranformar:'))
escolha = int(input('Escolha a linguagem: \n\033[0;32m[1]Binario |\033[1;34m[2]Octal |\033[1;35m[3]Hexadecimal\033[0;0m\nSua escolha:'))
if escolha == 1:
    print('\033[0;32mSeu número em binário é: {}.'.format(bin(N)[2:]))
elif escolha == 2:
    print('\033[1;34mSeu número em Octal é {}.'.format(oct(N)[2:]))
elif escolha == 3:
    print('\033[1;35mSeu número em Hexadecimal é {}.'.format(hex(N))[2:])
else:
    print('\033[1;31mOpção invalida.\033[1;31m')