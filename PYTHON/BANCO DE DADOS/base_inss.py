import os
os.system("cls")


bases_inss = [1320,2571.29,3856.94,7507.49]
porcento = [7.5,9,12,14]
desc = [0, 19.8, 96.94, 174.08]

valor_inss=0
global x
x=0
def inss(valor):
    x=0
    for i in bases_inss:
        if valor <= i:
          valor_inss = (valor*porcento[x]/100)-(desc[x])
          return valor_inss
          
        else:
          x += 1
        

inss(500)


