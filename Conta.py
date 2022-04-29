from Titular import Titular

class Conta():

    def __init__(self, titular=Titular, saldo=0):
        self.__titular = titular
        self.__saldo = saldo

    def sacar(self, valor):
        self.__saldo -= valor

    def depositar(self, valor):
        self.__saldo += valor

    def obterSaldo(self):
        return self.__saldo

    def obterTitular(self):
        return self.__titular
