#importando a função para ver o ano
from datetime import datetime

#verifica o ano de nascimento da pessoa
ano_de_nascimento = int(input("Digite seu ano de nascimento: "))
#calcula ano atual - ano de nascimento para descobrir a idade da pessoa
idade = datetime.now().year - ano_de_nascimento
#mostra na tela a idade da pessoa
print(f'Com {idade}, sua classificação é: ')

#verificação de qual classificação a pessoa se enquadra
if idade <= 9:
    print(f'Mirim')
elif idade <= 14:
    print(f'Infantil')
elif idade <= 19:
    print(f'Junior')
elif idade <= 25:
    print(f'Sênior')
else:
    print(f'Master')