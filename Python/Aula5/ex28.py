import random

numero2 = int(input('Esolha um numero entre 0 a 5 e veja se voce venceu: '))
escolhido = random.randint(0, 5)
if escolhido == numero2:
    print('Voce acertou')
else:
    print('Voce errou')
    print(f'O numero era {escolhido}')