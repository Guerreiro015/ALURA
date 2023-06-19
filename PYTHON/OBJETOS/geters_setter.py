#PROPIEDADES OS GETTERS E SETTER SERVEM PARA ADICIONAR PROPIEDADES AOS OBJETOS


from msilib.schema import Property


class banco:
    import os
    os.system("cls")
    def __init__(self,numero,nome,saldo,limite):
        self.__nome = nome
        self.__numero = numero
        self.__saldo = saldo
       # self.__limite = limite
       
    
         
    @Property
    def nome(self):
        return self.__nome
    
    @nome.setter 
    def nome(self,valor):
        if type(valor) == type(str()):
            print("Deve ser um vaor numerico")
        else:
        self.__nome = valor

    


conta = banco(123, "Nico", 55.5, 1000.0)

conta.pega_saldo()

conta.devolve_nome()

conta.retorna_limite()

