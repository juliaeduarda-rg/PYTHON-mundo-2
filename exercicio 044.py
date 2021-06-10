preço = float(input('Quanto é o seu produto?'))
E = int(input('Qual a forma de pagamento:\n\033[0;32m[1]A vista no dinheiro/cheque |\033[0;32m'
          '\033[1;31m[2]A vista no cartão |\033[1;31m'
          '\033[1;34m[3]Em até 2x no cartão |\033[1;34m'
          '\033[1;36m[4]Em 3x ou mais no cartão.\n'))
if E == 1:
    print('O valor de pagamento do produto é {:.2f}, com 10% de desconto.'.format(preço - (preço * 10/100)))
elif E == 2:
    print('O valor de pagamento do seu produto é {:.2f}, com 5% de desconto'.format(preço - (preço * 5/100)))
elif E == 3:
    print('O valor de pagamento do seu produto é {:.2f}'.format(preço))
elif E == 4:
    print('\033[1;97mO valor de pagamento do seu produto é {:.2f}'.format(preço + (preço * 20/100)))
else:
    print('\033[1;31mOPÇÃO INVALIDA!\033[1;31m')