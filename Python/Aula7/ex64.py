#funciona do mesmo jeito que numero = 0
#count = 0
#soma = 0
numero = count= soma = 0
numero = int(input('Digite um número [999 para parar]: '))
while numero != 999:
    soma += numero
    count += 1
    numero = int(input('Digite um número [999 para parar]: '))
print(f'Você digitou {count} e a soma entre eles foi {soma}.')