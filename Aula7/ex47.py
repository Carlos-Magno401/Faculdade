#recebe o numero que a pessoa quer ver
numero = int(input("Digite um número: "))
#laço for que vai ver se o resto da divisão é 0 para mostrar na tela do usuario
for count in range (0, numero+1):
    if count%2==0:
        print(count)
print('Acabou')

#forma mais eficiente de fazer isso:
for count in range (2, numero+1, 2):
    print(count)
print('Acabou')