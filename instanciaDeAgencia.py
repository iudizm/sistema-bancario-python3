from Agencia import Agencia
from Conta import Conta
from Titular import Titular

conta1 = Conta(Titular("Iudi Z.", 1420), 500)
conta2 = Conta(Titular("Sophia C.", 1669), 1000)

agência = Agencia([conta1, conta2])

lista_de_clientes = agência.listarTitulares()

print(lista_de_clientes)
