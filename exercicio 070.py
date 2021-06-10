cont2 = total = menor = cont = 0
resp = nomev = ''
while True:
    produtos = str(input('Qual o nome do produto?'))
    preco = float(input('Qual o preço do produto?'))
    cont2 += 1
    total += preco
    if preco > 1000:
        cont += 1
    if cont2 == 1:
        menor = preco
        nomev = produtos
    else:
        if preco < menor:
            menor = preco
            nomev = produtos
    resp = str(input('Deseja continuar? [S x N]'))
    if resp in 'nN':
        break
    if resp not in 'NnSs':
        resp = str(input('Deseja continuar? [S x N]'))
print(f'O total dos gastos da compra é R${total:.2f}. {cont} produtos custam mais de 1000 reais. O menor preço foi o produto {nomev} por {menor:.2f}')
