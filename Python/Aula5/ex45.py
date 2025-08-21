#importa a função para escolher um numero aleatorio
from random import randint
#recebe a jogada da pessoa
jogador = int(input('''
Escolha sua opção:
[0] para papel
[1] para tesoura
[2] para pedra
 '''))
itens = ('Papel', 'Tesoura', 'Pedra') #lista das jogadas
computador = randint(0, 2) #escolhe um numero aleatorio entre 0 e 2

#descobre quem ganhou
if jogador != itens: #verifica se a pessoa escolheu um numero que não estava nas opçoes
    print('Jogada invalida') 
if jogador == computador: #verifica se o computador e a pessoa jogaram o mesmo valor
    print(f'O jogador escolheu {itens[jogador]} e o computador tambem escolheu {itens[computador]}, deu empate')
if jogador != computador: #resultado das jogadas
    if jogador == 0 and computador == 1:
        print(f'Você jogou {itens[jogador]} e o computador jogou {itens[computador]}, quem ganha é o computador com {itens[computador]}')
    elif jogador == 1 and computador == 2:
        print(f'Você jogou {itens[jogador]} e o computador jogou {itens[computador]}, quem ganha é o computador com {itens[computador]}')
    elif jogador == 2 and computador == 0:
        print(f'Você jogou {itens[jogador]} e o computador jogou {itens[computador]}, quem ganha é o computador com {itens[computador]}')
    else:
        print(f'Você jogou {itens[jogador]} e o computador jogou {itens[computador]}, quem ganhou foi voce com {itens[jogador]}')