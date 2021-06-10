resposta = ''
soma = 0
maior = 0
menor = 0
n = 0
cont = 0
while resposta != 'N':
    n = int(input('Quantos números deseja digitar?'))
    for c in range(0,n):
        numero = int(input('Digite um numero:'))
        soma += numero
        cont += 1
        if c == 0:
            maior = numero
            menor = numero
        else:
            if numero > maior:
                maior = numero
            if numero < menor:
                menor = numero
    print('A media foi de {:.2f}'.format(soma / cont))
    print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
    resposta = str(input('Deseja continuar?[S]x[N]').strip().upper())