#PROPIEDADES OS GETTERS E SETTER SERVEM PARA ADICIONAR PROPIEDADES AOS OBJETOS


from msilib.schema import Property


class banco:
    import os
    os.system("cls")
    def __init__(self,numero,titular,saldo,limite):
        self.__titular = titular
        self.__numero = numero
        self.__saldo = saldo
        self.__limite = limite
       
    
         
    @Property
    def titular(self):
        return self.__titular
    @property
    def limite(self):
        return self.__limite

    


conta = banco(123, "Nico", 55.5, 1000.0)

conta.pega_saldo()

conta.devolve_titular()

conta.retorna_limite()

