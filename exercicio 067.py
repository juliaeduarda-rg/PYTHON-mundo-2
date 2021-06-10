print('<'*20)
print('\033[1;36mTABUADA')
print('\033[0;0m>'*20)
while True:
    n = int(input('Qual número você deseja multiplicar?'))
    print('~'*12)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} . {c} = {n * c}')
    print('~'*12)