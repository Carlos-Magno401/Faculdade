# sobrecarga

def sobrecarga(nome, numero=None):
    print(nome)
    if numero:
        print(numero)


print('Primeira execução')
sobrecarga('Rafael') 

print('Segunda execução')
sobrecarga('Rafael', 10)