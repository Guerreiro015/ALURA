import re

class validar_tel:
    def __init__(self,telefone):
     self.telefone = telefone
     if self.validar(self.telefone):
      print(f'Telefone {self.telefone} validado com sucesso')
     else:
      print(f' Número de telefone inválido')

    def validar(self,valor):
        padrao = "[0-9]{2}[0-9]{4,5}[0-9]{4}"
        resposta = re.findall(padrao,valor)
        if resposta:
            return True
        else:
            return False