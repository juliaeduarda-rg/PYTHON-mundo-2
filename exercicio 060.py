numero = int(input('Escreva o numero que deseja fatorear:'))
fatorial = 1
n = 1
while numero != 1:
    fatorial = fatorial * numero
    numero = numero - 1
print('Seu número fatorial é {}'.format(fatorial))