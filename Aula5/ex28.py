import random

lista = [0, 1, 2, 3, 4, 5]
numero2 = int(input('Esolha um numero entre 0 a 5 e veja se voce venceu: '))
escolhido = random.choice(lista)
if escolhido == numero2:
    print('Voce acertou')
else:
    print('Voce errou')
    print(f'O numero era {escolhido}')