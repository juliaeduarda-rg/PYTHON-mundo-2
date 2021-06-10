r1 = float(input('1º reta:'))
r2 = float(input('2º reta:'))
r3 = float(input('3º reta:'))
if r1 + r2 > r3:
    print('Pode ser um triangulo')
    if r1 == r2 == r3:
        print('É um triângulo: Equilatéro.')
    elif r1 == r2 or r2 == r3 or r3 == r1:
        print('É um triângulo: Isóceles. ')
    elif r1 != r2 != r3:
        print('É um triângulo: Escaleno.')
else:
    print('não pode ser um triangulo')
