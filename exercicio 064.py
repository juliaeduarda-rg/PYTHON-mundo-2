ni = 0
cont = 0
result = 0
ni = int(input('Escreva o número que deseja (Caso não deseje mais números escreva 999):'))
while ni != 999:
    cont += 1
    result += ni
    ni = int(input('Escreva o número que deseja (Caso não deseje mais números escreva 999):'))
else:
    print('O resultado de todos os números é {} e foram {} números digitados.'.format(result, cont))