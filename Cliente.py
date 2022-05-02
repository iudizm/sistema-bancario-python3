import Pessoa

class Cliente(Pessoa):

    def __init__(self, nome="", ano_de_nascimento=0):
        super().__init__(nome, ano_de_nascimento)
