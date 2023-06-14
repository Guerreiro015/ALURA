
class banco:
    def __init__(self,nome,numero,saldo,limite):
        self.nome = nome
        self.CC = numero
        self.saldo = saldo
        self.limite = limite

    def cria_conta(numero, nome, saldo, limite):
        conta = {"numero": numero, "nome": nome , "saldo": saldo, "limite": limite}
        return conta

    def cadastro(nome):
        print("O cliente {} foi cadastrado com sucesso ".format(nome))
