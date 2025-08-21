#recebe o incio pro laço for
primerio_termo = int(input("Primeiro termo: ")) 
#recebe quantos passos serão dados
razao = int(input("Razão: "))
#calcula o final do laço for
final = primerio_termo+(10-1)*razao
#for que faz uma progressão aritmética
for count in range (primerio_termo,final+razao, razao ):
    print(count)
print('Acabou')