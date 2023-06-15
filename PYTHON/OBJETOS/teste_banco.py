
class banco:
    def __init__(self,nome,numero,saldo,limite):
        self.nome = nome
        self.numero = numero
        self.saldo = saldo
        self.limite = limite


    def deposito(self,deposito):
        if deposito > 500:
            print("saldo positivo")
        elif deposito < 500:
            print("saldo negativo")


cliente1 = banco("antonio",111,100,500)
print(cliente1.nome)
cliente1.deposito(600)
cliente2 = banco("lucas",222,1000,5050)
print(cliente2.nome)
cliente2.deposito(200)



