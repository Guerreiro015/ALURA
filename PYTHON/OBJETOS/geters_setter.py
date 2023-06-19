#PROPIEDADES OS GETTERS E SETTER SERVEM PARA ADICIONAR PROPIEDADES AOS OBJETOS
import os
os.system("cls")

class Persona:
    def __init__(self, name,limite):
        self._name = name
        self._limite = limite

    @property
    def name(self):
        print('\nMostrando o name')
        return self._name

    @name.setter
    def name(self, value):
        if type(value) != type(str()):
            print(" O nome não pode ser mumero ")
        else:
            print('\nTrocando name para ',value)
            self._name = value

    # @name.deleter
    # def name(self):
    #     print('Deleting name')
    #     del self._name



    @property
    def limite(self):
        print('\nMostrando o limite')
        return self._limite

    @limite.setter
    def limite(self, value):
        if type(value) == type(str()):
            print(" O nome não pode ser mumero ")
        else:
            print('\nTrocando limite para ',value)
            self._limite = value

li = Persona('Luana',0)
print('The limite is:', li.limite)
li.limite = 50
print('The o limite is:', li.limite)
#del p.name

pessoa = Persona('Luana',0)
print('O nome é :', pessoa.name)
pessoa.name = 50
print('O nome é :', pessoa.name)
pessoa.name = "Francsica"
print('O nome á : ', pessoa.name)
#del p.name



 