from Agencia import Agencia
from Cliente import Cliente
from Conta import Conta

def listarClientesDeAgencia(agencia):
    print("Lista de Clientes:")
    lista_de_clientes = agencia.listarTitulares()
    for cliente in lista_de_clientes:
        print(cliente)

def criaClientesDeTeste(quantidade):
    clientes = []
    for i in range(0, quantidade):
        conta = Conta(Cliente("Mussum Ipsum", 1979, "Rua dos Loucos, nº 0", id=i), 1000)
        clientes.append(conta)
        i += 1
    return clientes

def criaAgenciaDeTeste(contas = criaClientesDeTeste(5)):
    return Agencia(contas)

agencia = criaAgenciaDeTeste()
listarClientesDeAgencia(agencia)