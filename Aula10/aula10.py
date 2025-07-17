#texto=['abc']
#print('n' not in texto)

#a, b=[1, 2]
#print(a)

# pode ser usado em metodos para ver um dicionario
lista=[('a', 1), ('b', 2)]
for letra, numero in lista:
    print(f'{letra}: {numero}')

#conceito de passagem de argumentos (não aplicavel no python desse jeito)
#o python sempre vai passar o objeto por referencia, mas existe objetos mutaveis e imutaveis
#def my_function(n):
#    ...
#x=23
#my_function(x) # val
#my_function(x) # ref  

def teste(n,s):
    n = n +2
    s[0] = s[0] + 1
    return
n1 = 1
lista =[1]
teste(n1, lista)
print(f'{n1, lista} fim')

