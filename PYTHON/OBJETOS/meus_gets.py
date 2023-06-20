import os
os.system("cls")

class banco:
    def __init__(self,titular,vendas):
        self._titular = titular
        self._vendas = vendas

@property
def titular(self):
    return self._titular

@titular.setter
def titular(self,valor):
    self._titular = valor
    print(f"\nTitular alterado para {self._titular}")



cliente = banco("Lucas",0)

print(f'\nCliente {cliente._titular} foi cadastrado com sucesso')
cliente.titular = "Luana"
print(f"\nTitular é  {cliente._titular}")

cliente1 = banco("Antonio",0)

print(f'\nCliente {cliente1._titular} foi cadastrado com sucesso')
cliente1.titular = "Luana"
print(f"\nTitular é  {cliente1._titular}")
