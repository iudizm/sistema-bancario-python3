class Pessoa():

    def __init__(self, nome="", ano_de_nascimento=0, cpf=0, endereco=""):
        self.__cpf = cpf
        self.__nome = nome
        self.__ano_de_nascimento = ano_de_nascimento
        self.__endereco = endereco

    def obterNome(self):
        return self.__nome

    def obterAnoDeNascimento(self):
        return self.__ano_de_nascimento

    def obterEndereco(self):
        return self.__endereco
