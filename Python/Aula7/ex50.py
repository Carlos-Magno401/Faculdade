#variavel feita para ser um contador
contador = 0
#laço for de repetição para somar apenas os numeros pares digitados
for count in range(1, 7):
    numero=int(input("Digite um numero: "))
    if numero % 2== 0:
        contador = contador + numero
#mostra na tela qual foi o resultado da soma 
print(f'No final, a soma de todos os numeros pares deu: {contador}')