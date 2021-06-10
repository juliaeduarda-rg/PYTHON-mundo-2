menor = 0
maior = 0
for c in range(0,5):
    p = float(input('Qual seu peso?'))
    if c == 0:
        maior = p
        menor = p
    else:
        if p > maior:
            maior = p
        if p < menor:
            menor = p
print('''O maior peso foi {}.
E o menor foi {}.'''.format(maior, menor))