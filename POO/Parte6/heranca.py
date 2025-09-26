class Mae:      # Mamifero
    def __init__(self):
        print('executando o init de Mae')    


class Filha(Mae):       # Felino
    def __init__(self):
        print('executando o init de Filha')


class Neta(Filha):      # Gato
    def __init__(self):
        print('executando o init de Neta')


class MeusInteiro(int):
    pass

class MeuDicionario(dict):
    def metodo_extra(selg):
        pass

