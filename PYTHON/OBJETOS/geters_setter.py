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
    def name(self, value):
        if type(value) != type(str()):
            print('''\n A troca de nome não foi possível
            nome não pode ser mumero\n ''')
        else:
            print('\nTrocando nome para ',value)
            self._name = value.upper()


    @property
    def limite(self):
        return self._limite

    @limite.setter
    def limite(self, value):
        if type(value) == type(str()):
            print('''\n Tentativa de aumentar limite falhou
            O limite não pode ser strings \n''')
        else:
            print('\nTrocando limite para ',value)
            self._limite = value

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self,value):
        if type(value) != type(int()):
             print('''\n Deposito não reaizado
            O valor não pode ser strings \n''')
        else:     
            self._saldo += value
            print(f"\nFazendo um depósito de R$ {value}")
            print(f"Seu novo saldo é {self._saldo}")


limi = Persona('Luana',100,50)
print(f'\nA cliente {limi.name} foi cadastrao com um limite de: {limi.limite}')
limi.limite = "asd"
print(f'O novo limite é:{limi.limite}')
#del p.limite


pessoa = Persona('Lucas',500,100)
print(f'\nO cliente {pessoa.name} foi cadastrado com sucesso, seu limite é: {pessoa.limite}')
pessoa.name = 3445
print('O nome é :', pessoa.name)
pessoa.name = "Francisca"
print(f'O nome é : {pessoa.name} e seu saldo é R$: {pessoa.saldo}')

pessoa.saldo = "noem"

print(f'O nome é : {pessoa.name} e seu saldo é R$: {pessoa.saldo}')


#del p.name



 