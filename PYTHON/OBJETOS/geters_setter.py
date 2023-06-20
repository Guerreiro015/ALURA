#PROPIEDADES OS GETTERS E SETTER SERVEM PARA ADICIONAR PROPIEDADES AOS OBJETOS
 # @name.deleter
    # def name(self):
    #     print('Deleting name')
    #     del self._name

import os
os.system("cls")

class Persona:
    def __init__(self, name,limite,saldo):
        self._name = name
        self._limite = limite
        self._saldo = saldo

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, valor):
        if type(valor) != type(str()):
            print('''\n A troca de nome não foi possível
            nome não pode ser mumero\n ''')
        else:
            print('\nTrocando nome para ',valor)
            self._name = valor.title()


    @property
    def limite(self):
        return self._limite

    @limite.setter
    def limite(self, valor):
        if type(valor) == type(str()):
            print('''\n Tentativa de aumentar limite falhou
            O limite não pode ser strings \n''')
        else:
            print('\nTrocando limite para ',valor)
            self._limite = valor

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self,valor):
        if type(valor) != type(int()):
             print('''\n Deposito não realizado
            O valor não pode ser strings \n''')
        else:     
            self._saldo += valor
            print(f"\nFazendo um depósito de R$ {valor}")
            print(f"Seu novo saldo é {self._saldo}")


limi = Persona('Luana',100,50)
print(f'\nA cliente {limi.name} foi cadastrao com um limite de: {limi.limite}')
limi.limite = "asd"
print(f'O novo limite é:{limi.limite}')
#del p.limite


pessoa = Persona('Antonio',500,100)
print(f'\nO cliente {pessoa.name} foi cadastrado com sucesso, seu limite é: {pessoa.limite}')
pessoa.name = 1111
print('O nome é :', pessoa.name)
pessoa.name = "Francisca"
print(f'O nome é : {pessoa.name} e seu saldo é R$: {pessoa.saldo}')

pessoa.saldo = "noem"

print(f'O nome é : {pessoa.name} e seu saldo é R$: {pessoa.saldo}')


#del p.name



 