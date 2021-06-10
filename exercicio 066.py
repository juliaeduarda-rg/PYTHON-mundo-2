s = 0
n = 0
cont = 0
n = int(input('Digite um numero:'))
while True:
    s += n
    n = int(input('Digite um numero:'))
    cont += 1
    if n == 999:
        break
print(f'{cont} números foram digitados e a soma vale {s}')