r = ''
maior = idade = homem = mulher = 0
sexo = ''
while True:
    idade = int(input('Idade:'))
    if idade > 18:
        maior += 1
    sexo = str(input('Sexo [M x F]:'))
    while sexo not in 'FfMm':
        sexo = str(input('Sexo [M X F]'))
    if sexo in 'Mm':
        homem += 1
    if sexo in 'Ff' and idade < 20:
        mulher += 1
    r = input('Deseja continuar? [S x N]')
    if r in 'Nn':
        break
print(f'{maior} pessoas tem mais de 18 anos. {homem} homens foram cadastrados. {mulher} mulheres tem menos de 20 anos.')