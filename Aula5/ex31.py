km = float(input('Digite quantos km vão ser de viagem: '))
if km <= 200:
    valor = km*0.50
    print(f'O valor da sua viagem deu R${valor}')
else:
    valor = km*0.45
    print(f'Como a viagem é maior, então o valor deu R${valor}')

#tbm tem como fazer desse jeito: 
#valor = km*0.50 if km  <= 200 else km*0.45