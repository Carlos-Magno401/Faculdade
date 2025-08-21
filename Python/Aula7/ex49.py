#recebe um valor escolhido pela pessoa
contador = int(input("Digite um numero para ver a tabuada: "))
#tabuada em laço for
for count in range (1, 11):
    print(f'{contador} X {count} = {count*contador}')