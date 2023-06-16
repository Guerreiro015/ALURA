class data():
    import os
    os.system("cls")
    def __init__(self,dia,mes,ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano
    
   
    def data_formadada(self):
      print (self.dia,"/",self.mes,"/",self.ano)
     

d=data(21,11,2007)
d.data_formadada()





