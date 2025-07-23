#contador incial
maisvelho = 0
maisnovo = 0
#for que tem um contador interno verificando quantas pessoas tem de maior e menor idade
for count in range(1, 9):
    ano = int(input(f"Em que ano a {count}° pessoa nasceu? "))
    if ano >= 2000:
        maisnovo += 1
    else:
        maisvelho += 1
#mostra na tela quantas pessoas mais velhas e mais novas tem
print(f'Ao todo tempos {maisvelho} pessoas maiores de idade.\nE Também tivemos {maisnovo} pessoas menores de idade.')