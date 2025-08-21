salario = int(input('INFORME O SALÁRIO:'))

if salario > 1250:
    print(f'Seu salário é R${salario + (salario*10/100)}')

if salario <= 1250:
    print(f'Seu salário é R${salario + (salario*15/100)}')

print(f'Salario novo é: {salario}')