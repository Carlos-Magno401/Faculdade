notas_sala = [[5.5, 7.0, 8.7],
                [8.0, 6.0, 9.2],
                [7.8, 8.3, 8.5],
                ]

medias=[]

for notas_aluno in notas_sala:
    soma=0
    cont=0
    for nota in notas_aluno:
        soma += nota
        cont += 1
    media = soma / cont
    medias.append(media)
print(medias)





#mudança na variavel lista por causa do .append()
lista=[5, 6]
lista2= lista
print(lista)
lista2.append(7)
print(lista)