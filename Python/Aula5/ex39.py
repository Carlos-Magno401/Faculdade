#importando o modulo para saber ano
from datetime import datetime

#recebe o ano que a pessoa nasceu
ano_nas = int(input("Ano de Nascimento: "))
#recebe o ano atual do computador
ano_atual= datetime.now().year
#calcula a idade da pessoa
idade= ano_atual-ano_nas

print(f'Quem nasceu em {ano_nas} tem {idade} anos em {ano_atual}')
if idade > 18:
    print(f'Você já deveria ter se alistado há {idade - 18} anos')
elif idade <18:
    print(f'Falta ainda {18-idade} para você se alistar, você vai se alistar em {ano_atual+(18-idade)}')
elif idade==18:
    print('Aliste-se imediatamente')
