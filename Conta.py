from Cliente import Cliente

class Conta():

    def __init__(self, titular=Cliente, saldo_inicial=0):
        self.__titular = titular
        self.__saldo = saldo_inicial

    def sacar(self, valor):
        self.__saldo -= valor

    def depositar(self, valor):
        self.__saldo += valor

    def obterSaldo(self):
        return self.__saldo

    def obterTitular(self):
        return self.__titular

    def transferir(self, valor, conta_destino):
        self.sacar(valor)
        conta_destino.depositar(valor)