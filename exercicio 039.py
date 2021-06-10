import datetime
ano = int(input('Ano de nascimento:'))
hoje = int(datetime.datetime.now().year)
idade = hoje - ano
if idade<18:
    print('Você não tem idade para se alistar. Você tem {} anos, faltam ainda {} anos!'.format(idade, (18 - idade)))
    print('Você irá se alistar em {}'.format(ano + 18))
elif idade == 18:
    print('Você já tem 18 anos, é hora de se alistar!')
elif idade>18:
    print('Já passou o tempo de se alistar. Você tem {} anos. Passaram {} anos.'.format(idade, (idade-18)))
    print('Você deveria ter se alistado em {}'.format(ano + 18))