ano = int(input('Fale um ano: '))
if ano%4==0 and ano%400==0 and ano%100==01:
    print('É bissexto')
else:
    print('Não é bissexto')