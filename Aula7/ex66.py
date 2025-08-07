soma = count = 0
while True:
    num = int(input('Digite um valor (999 para parar): '))
    if num == 999:
        break
    count += 1
    soma += num
print(f'A soma dos valroes foi {soma}')