A = float(input('Qual sua altura?'))
P = float(input('Qual seu peso?'))
IMC = (P / (A**2))
if IMC <= 18.5:
    print('Você está abaixo do peso.')
elif 18.5< IMC <=25:
    print('Você está no seu peso ideal.')
elif 25 < IMC <= 40:
    print('Você está obeso.')
elif IMC >40:
    print('\033[1;31mVocê está com obesidade morbida.\033[1;31m')