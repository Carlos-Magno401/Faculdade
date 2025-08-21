#contadores base
contador_mulher = 0
contador_media = 0
idade_maior = 0
contador_nome = ''
#laço for que recebe nome, idade e sexo da pessoa e guarda nos contadores
for count in range (1, 5):
    nome = str(input("Nome: "))
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: ")).upper()
    contador_media += idade
    if idade > idade_maior:
        idade_maior = idade
        contador_nome = nome
    if sexo == 'F' and idade < 20:
        contador_mulher += 1

media = contador_media/4 #pega a media da idade das pessoas
#Mostra na tela as informaçoes
print(f'A média de idade do grupo é de {media} anos.')
print(f'A pessoa mais velha tem {idade_maior} e se chama {contador_nome}.')
print(f'Ao todo são {contador_mulher} mulheres com menos de 20 anos')