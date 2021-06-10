valorcasa = float(input('Qual o valor da casa desejada?'))
s = float(input('Qual o valor do seu salário?'))
ano = int(input('Em quantos anos pretende comprar a casa?'))
emp = valorcasa / (ano * 12)
print('O valor mensal da casa seria de: {:.2f} por mês, em {} anos. por uma casa de valor {:.2f}. Sendo seu salário de R${:.2f}'.format(emp, ano, valorcasa, s))
if emp > s * 30 / 100:
    print('\033[1;31mSeu emprestimo foi negado!\033[1;31m')
else:
    print('\033[0;32mSeu emprestimo foi aceito!\033[0;32m')