resp = 'S'
soma = quant = media = maior = menos = 0
while resp in 'Ss':
    numero = int(input('Digite um número: '))
    soma += numero
    quant += 1
    if quant == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    resp = str(input('Quer continuar [S/N]? ')).upper().strip()[0]
media = soma/quant
print(f'Voce digitou {quant} numeros e a média foi {media}')
print(f'O maior valor foi {maior} e o menor foi {menor}.')