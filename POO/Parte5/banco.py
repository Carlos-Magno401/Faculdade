class Conta:
    def __init__(self, numero, titular):
        self.numero = numero
        self.titular = titular
        self.__saldo = 0

    # Método acessor (get)
    #def get_saldo(self):
    #    return self.__saldo

    # Método modificador (set)
    #def set_saldo(self, valor):
     #   self.__saldo = valor

    @property
    def saldo(self):
        return self.__saldo

    def depositar(self, valor):
        if valor < 0:
            return 'Valor deve ser positivo'
        self.__saldo += valor

    def sacar(self, valor):
        if valor < 0:
            return 'Valor deve ser positivo'
        if valor > self.__saldo:
            return 'Saldo insuficiente'
        self.__saldo -= valor

if __name__ == '__main__':
    conta1 = Conta(1, 'Rafael')
