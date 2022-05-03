import Pessoa

class Cliente(Pessoa.Pessoa):

    def __init__(self, nome="", ano_de_nascimento=0, endereco="", id=0, id_gerente=0):
        super().__init__(nome, ano_de_nascimento, endereco)
        self.__id = id
        self.__id_gerente = id_gerente

        def obterGerente(self):
            return self.__id_gerente

        def obterId(self):
            return self.__id
