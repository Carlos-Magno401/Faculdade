numero = int(input('Escolha um numero inteiro: '))
escolha = int(input('Digite 1 para BINÁRIO, 2 para OCTAL e para HEXADECIMAL'))

if escolha == 1:
    print(f'{numero} convertido para binario é igual a {bin(numero)[2:]}')
elif escolha == 2:
    print(f'{numero} convertido para octal é igual a {oct(numero)[2:]}')
elif escolha == 3:
    print(f'{numero} convertido para hexadecimal {exec(numero)[2:]}')
else: 
    print('Não existe essa opção')