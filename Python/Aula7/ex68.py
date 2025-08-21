from random import randint

v = 0

while True:
    jogador = int(input('Dige um valor: '))
    computador = randint (0, 10)
    total = jogador + computador
    tipo= ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}')
    print('Deu par' if total % 2==0 else 'Deu Ímpar')
    