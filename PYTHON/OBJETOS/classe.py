class funci():
    def __init__(self,nome):
        self.nome = nome
        self.vendas = 0

    def vendeu(self,vendas):
        self.vendas = vendas

    def meta(self,meta):
        if self.vendas > meta:
            print(f" A meta de {self.nome},Bateu meta")
        else:
            print(self.nome,"Não bateu meta")






