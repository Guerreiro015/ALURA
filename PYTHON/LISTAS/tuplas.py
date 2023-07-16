import os
os.system("cls")

conta = ("ana",1000)

# As tuplas usam os parenteses em vez de colchetes
# As tuplas não posem set alteradas

def deposito(valor):
    saldo = conta[1]+valor
    nome = conta[0]
    return (nome,saldo)

print(f"Conta antes do depósito {conta}")

conta = deposito(500)

print(f"Conta depois do depósito {conta}")

# Conclusão não conseguimos modificar mas conseguimos criar outra tupla com os valores alterados
