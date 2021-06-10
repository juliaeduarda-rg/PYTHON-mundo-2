s = str(input('Qual seu sexo? [M]x[F]')).strip().upper()[0]
while s not in 'MmFf':
    s = str(input('Dado inválido. Escreva novamente.')).strip().upper()[0]
print('Certo! Sexo {} registrado com sucesso!'.format(s))