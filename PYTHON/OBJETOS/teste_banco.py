
class banco:
    import os
    os.system("cls")
    def __init__(self,nome,numero,saldo,limite):
        self.nome = nome
        self.numero = numero
        self.saldo = saldo
        self.limite = limite


    def deposito(self,depositado):
        self.depositado = depositado
        self.saldo += depositado
        

cliente1 = banco("Antonio",111,100,500)
print(cliente1.nome)
print(cliente1.saldo)
print(f"O cliente {cliente1.nome} abriu a conta com R$: {cliente1.saldo}")

deposito_cliente1 = int(input(f"Digite o Valor do depósito para o {cliente1.nome}, R$: "))

cliente1.deposito(deposito_cliente1)

print(f"O cliente {cliente1.nome} depositou {deposito_cliente1} e ficou com R$: {cliente1.saldo} de saldo")


cliente2 = banco("lucas",222,1000,5050)
print(cliente2.nome)
print(cliente2.saldo)

deposito_cliente2 = int(input(f"Digite o Valor do depósito para o {cliente2.nome}, R$: "))

cliente2.deposito(deposito_cliente2)

print(f"O cliente {cliente2.nome} depositou {deposito_cliente2} e ficou com R$: {cliente2.saldo} de saldo")


cliente2.deposito(200)
print(cliente2.saldo)




