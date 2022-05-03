import Pessoa
from TipoDeFuncionario import TipoDeFuncionario

class Funcionario(Pessoa.Pessoa):
    
    def __init__(self, nome="", ano_de_nascimento=0, cpf=0, endereco="", id=0):
        super().__init__(nome, ano_de_nascimento, cpf, endereco)
        self.__id = id
        self.__tipo = TipoDeFuncionario.COMUM

    def obterId(self):
        return self.__id

    def obterTipo(self):
        return self.__tipo