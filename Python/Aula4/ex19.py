import random
n1=input('Primeiro aluno: ')
n2=input('segundo aluno: ')
n3=input('Terceiro aluno: ')
n4=input('Quarto aluno: ')

lista=[n1,n2,n3,n4]
escolhido=random.choice(lista)
print(f'O escolhido foi {escolhido}')