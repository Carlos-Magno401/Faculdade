import math
n=8_000_000_000
print(math.log(n, 2))



 #Parâmetros posicionais


#def recepcao_clente(nome, senha):
#    print(f'Olá {nome}, sua senha é {senha}')

#nome = 'Julia'
#senha = 25
#recepcao_clente(nome, senha)


#Parâmetros nomeados

def recepcao_cliente(nome, senha):
    print(f'Olá {nome}, sua senha é {senha}')

nome = 'Julia'
senha = 25
recepcao_cliente(senha=senha, nome=nome)



#Parâmetros opcionais
def recepcao_client(nome, senha=1):
    print(f'Olá {nome}, sua senha é {senha}')

recepcao_client('Megan')