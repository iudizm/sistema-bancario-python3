import Funcionario
from TipoDeFuncionario import TipoDeFuncionario

class Gerente(Funcionario.Funcionario):

    def __init__(self, nome="", ano_de_nascimento=0, cpf=0, endereco="", id=0):
        super().__init__(nome, ano_de_nascimento, cpf, endereco, id)
        self.__tipo = TipoDeFuncionario.GERENTE
    