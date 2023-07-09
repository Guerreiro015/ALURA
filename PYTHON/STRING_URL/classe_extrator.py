import os
os.system("cls")
#VAMOS fazer um classe para fazer tosos saneamentos



class extrator:
    def __init__(self, url):
        self.url = self.limpa(url)
        self.validar(url)
        print(self.url)

    
    def limpa(self,url):
        if type(url) == str:
            return url.replace(" ","")
        else:
            url = ""

    def validar(self,url):
        if not self.url:
            print("O valor procurado não encontrado")
            #raise ValueError("Url esta vazia")
        
    def procura(self,valor):
        ini = self.url.find(valor)             # encontrar onde começa o valor de procura
        tamanho = len(valor)                   # encontrar o taanho o valor de procura
        resultado = self.url[ini+tamanho+1:]   # encontrar onde começa o valor procurado
        fim = resultado.find("&")              # encontrar onde termina o valor procurado
        final = resultado[:fim]                # Este é o resultado
        return final
    
dados = ("bytebank.     com/cambio?quantidade   =100&m    oedaOrigem=real&moedaDestino=dolar")

extrator_url = extrator(dados)

print(extrator_url.procura("quantidade"))
print(extrator_url.procura("moedaOrigem"))
print(extrator_url.procura("moedaDestino"))



