valor = float(input('Qual o valor da casa? '))
salario = float(input('Qual o salario? '))
anos = int(input('Quantos anos voce vai parcelar? '))
prestacao = valor/(anos*12)

if salario*0.30 <= prestacao:
    print('Infelizmente voce não pode pagar por isso')
else:
    print(f'Que ótimo, podemos comecar já! a valor a ser pago é {prestacao} ao mes')