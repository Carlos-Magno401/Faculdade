numero = int(input('Digite um número para calcular seu Fatorial: '))
count = numero
fatorial = 1
print(f'Calculando {numero}! = ', end='')
while count > 0:
    print(f'{count}', end='')
    print(' x ' if count > 1 else ' = ', end='')
    fatorial *= count
    count -= 1
print(f'{fatorial}')