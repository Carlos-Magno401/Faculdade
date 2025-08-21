#laço for que verefica o peso da pessoa e marca qual é o maior e qual é o menor
for count in range(1, 6):
    peso = float(input(f"Peso da {count}° pessoa: ")) #recebe os valores
    if count == 1:            #adicionando o peso base nos contadores
        maior = peso
        menor = peso
    else:
        if peso > maior :
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso lido foi de {maior}.\nO monor peso lido foi de {menor}.') #mostrando na tela os valores