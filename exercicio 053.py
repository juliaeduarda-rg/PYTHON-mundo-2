f1 = str(input('Escreva uma frase:').upper().replace(' ', '').strip())
f2 = (f1[::-1])
if f1 == f2:
    print('Sua frase é um palidromo.')
elif f2 != f2:
    print('Sua frase não é um palidromo.')
else:
    print('ERRO')