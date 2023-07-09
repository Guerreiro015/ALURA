import os
os.system("cls")
#VAMOS fazer um classe para fazer tosos saneamentos



class extrator:
    def __init__(self, url):
        self.url = self.limpa(url)
        self.validar(url)
        print(self.url)

    
    def limpa(self,url):
        return url.replace(" ","")

    def validar(self,url):
        if self.url == "":
            raise ValueError("Url esta vazia")
    def procura(self,valor):
        ini = self.url.find(valor)
        tamanho = len(valor)
        resultado = self.url[ini+tamanho:]
        return resultado
    
dados = ("bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar")
extrator_url = extrator(dados)

print(extrator_url.procura("quantidade"))



