print('Gerador de PA')
print('-='*10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
count = 1
mais = 10
while mais != 0:
    total = total + mais
    while count <= 10:
        print(f'{termo} -> ', end='')
        termo += razao
        count += 1
    print('Pausa')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Fim')