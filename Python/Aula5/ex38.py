numero1 = int(input('Digite um valor inteiro: '))
numero2 = int(input('Digite um segundo valor inteiro: '))

if numero1 > numero2:
    print(f'O numero {numero1} é maior')
elif numero2 > numero1:
    print(f'O numero {numero2} é maior')
else:
    print(f'Não existe valor maior, o numero {numero1} e o {numero2} são iguais')