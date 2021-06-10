media = 0
soma = 0
cont = 0
nomef = ''
maioridade = 0
nomev = ''
for p in range(1, 5):
    print('__________________________________________')
    nome = str(input('Seu nome:')).strip()
    idade = int(input('Sua idade:'))
    sexo = str(input('Sexo[M/F]:')).strip()
    soma += idade
    if p == 1 and sexo in 'Mm':
        maioridade = idade
        nomev = nome
    if sexo in 'Mm' and idade > maioridade:
        maioridade = idade
        nomev = nome
    if sexo in 'fF' and idade < 20:
            cont += 1
if cont == 1:
    print('{} mulher tem menos de 20 anos.'.format(cont))
else:
    print('{} mulheres tem menos de 20 anos.'.format(cont))
print('O home mais velho se chama {} e tem {} anos.'.format(nomev, maioridade))
media = soma / 4
print('A média de idade é {}'.format(media))
