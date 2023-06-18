#PROPIEDADES OS GETTERS E SETTER SERVEM PARA ADICIONAR PROPIEDADES AOS OBJETOS


class banco:
    import os
    os.system("cls")
    def __init__(self,numero,titular,saldo,limite):
        self._titular = titular
        self._numero = numero
        self._saldo = saldo
        self._limite = limite
       
    
       
   

    def pega_saldo(self,saldo):
        return self._limite

    def devolve_titular(self):
        return self.__titular

    def retorna_limite(self):
        return self.__limite



conta = banco(123, "Nico", 55.5, 1000.0)

conta.pega_saldo()

conta.devolve_titular()

conta.retorna_limite()

