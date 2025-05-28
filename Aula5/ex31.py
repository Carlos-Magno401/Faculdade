km = int(input('Digite quantos km vão ser de viagem: '))
if km <= 200:
    valor = km*0.50
    print(f'O valor da sua viagem deu R${valor}')
else:
    valor = km*0.45
    print(f'Como a viagem é maior, então o valor deu R${valor}')