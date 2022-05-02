from Agencia import Agencia
from Cliente import Cliente
from Conta import Conta

conta1 = Conta(Cliente("Iudi Z.", 1420), 500)
conta2 = Conta(Cliente("Sophia C.", 1669), 1000)

agência = Agencia([conta1, conta2])

lista_de_clientes = agência.listarTitulares()

print(lista_de_clientes)
