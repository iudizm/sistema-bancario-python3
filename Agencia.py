from Conta import Conta

class Agencia():

    def __init__(self, contas=[]):
        self.__registro = {}
        for conta in contas:
            titular = conta.obterTitular()
            self.__registro[titular.obterNome()] = conta

    def listarTitulares(self):
        return list(self.__registro)
    
    def obterContaDe(self, titular):
        return self.__registro[titular]

    def sacarDeConta(conta, valor):
        conta.sacar(valor)

    def depositarEmConta(conta, valor):
        conta.depositar(valor)

    def realizarTranferencia(origem, destino, valor):
        origem.transferir(valor, destino)