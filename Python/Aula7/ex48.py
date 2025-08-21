#contadores
cont = 0
soma = 0
#for que verifica todos os numeros impares multiplos de 3
for count in range (1, 501, 2):
    if count%3==0:
        soma = soma + count
        cont = cont + 1
print(f'A soma de todos esses resultados foi de: {soma}. E foi contado em {cont} vezes.')