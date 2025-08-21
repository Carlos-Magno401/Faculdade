#importando a funcão de espera 
from time import sleep
#recebe a contagem que a pessoa quer ver
numero = int(input("Numero: "))

#laço for de contagem regressiva com 0.5 segundo entre as contagens
for count in range (numero, -1, -1):
    print(count)
    sleep(0.5)
print('BOOM')