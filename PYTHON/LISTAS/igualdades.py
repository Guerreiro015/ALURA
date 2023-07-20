import os
os.system("cls")

import time


class banco:
    def __init__(self,nome):
        self._nome = nome
        self._saldo = 0
        
    def salario(self,valor):
        self._saldo +=valor

    def __str__(self) -> str:
        return f'Nome do cliente: {self._nome} Saldo: R$:  {self._saldo} '


Cliente1 = banco("Antonio")
Cliente2 = banco("Antonio")


print(Cliente1)
print(Cliente2)

Cliente1.salario(500)
Cliente2.salario(500)

if Cliente1 == Cliente2:
    print(Cliente1)
    print(Cliente2)
    print("Parecem iguais mas não são iguais") 
else:
    print("Parecem iguais mas não são iguais")

#######################################################################################

#para que os objetos retornem que são iguais precisamos usar a função (  __eq__ )

# def__init__(self, codigo):
#       self._codigo = codigo
#         self._saldo = 0

#     def__eq__(self, outro):
#       return self._codigo == outro._codigo


class banco:
    def __init__(self,nome):
        self._nome = nome
        self._saldo = 0
    
    def __eq__(self,outro):
        return self._nome == outro._nome
        
    def salario(self,valor):
        self._saldo +=valor
    
    def __str__(self) -> str:
        return f'Nome do cliente: {self._nome} Saldo: R$:  {self._saldo} '

       


Cliente1 = banco("Antonio")
Cliente2 = banco("Antonio")


print(Cliente1)
print(Cliente2)

Cliente1.salario(500)
Cliente2.salario(500)

if Cliente1 == Cliente2:
    print(Cliente1)
    print(Cliente2)
    print("Parecem iguais mas não são iguais") 
else:
    print("Parecem iguais mas não são iguais")



