I = int(input('Quantos anos você tem?'))
if I<9:
    print('Você está na categoria: MIRIM!')
elif 9<I<14:
    print('Você está na categoria: INFANTIL!')
elif 14<I<19:
    print('Você está na categoria: JUNIOR!')
elif 18<I<20:
    print('Você está na categoria: SÊNIOR!')
elif I>20:
    print('Você está na categoria: MASTER!')