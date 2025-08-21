#Recebe o um numero escolhido pelo usuario
numero = int(input("Digite um número: "))
#contador base
contador = 0
#for que verefica se o numero é primo. E tem 2 codigos de cor para melhor visualização
for count in range(1, numero+1):
    if numero%count==0:
        print('\33[33m', end=' ') #cor amarela se for divisivel
        contador = contador + 1 #ou contador+=1
    else:
        print('\033[31m', end=' ') #cor vermelha para se não for divizivel
    print(count, end=' ')
print(f'\n\033[mO numero {numero} foi divisivel {contador} vezes')
#indicador se é primo ou não
if contador == 2:
    print('Por isso ele é primo')
else:
    print('Por isso ele não é primo')