class Titular():

    def __init__(self, nome="", ano_de_nascimento=0):
        self.__nome = nome
        self.__ano_de_nascimento = ano_de_nascimento

    def obterNome(self):
        return self.__nome

    def obterAnoDeNascimento(self):
        return self.__ano_de_nascimento
