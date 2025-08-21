km = int(input('Qual foi a velocidade do carro em km? '))

if km <= 80:
    print('Tá tranquilo fi, não levou multa')
else:
    multa = (km - 80)*7
    print(f'multa, esquivalente a R${multa}')