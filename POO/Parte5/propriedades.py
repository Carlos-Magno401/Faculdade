class Teste:
    def __init__(self):
        self.__nome = ''
        self.cont = 0

    @property
    def nome(self):
        print(f'Executando a property... {self.cont}')
        return self.__nome
    
    @nome.setter
    def nome(self, novo_nome):
        print('executando o setter...')
        self.__nome = novo_nome