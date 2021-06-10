import datetime
maior = 0
menor = 0
for i in range(0,7):
    p = int(input('Em que ano você nasceu?'))
    p = datetime.date.today().year - p
    if p >= 20:
        maior += 1
    elif p <= 19:
        menor += 1
print('Em 7 pessoas temos: {} menores e {} maiores de 20 anos.'.format(menor, maior))