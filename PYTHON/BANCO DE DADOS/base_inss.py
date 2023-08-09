import os
os.system("cls")


bases_inss = [1320,2571.29,3856.94,7507.49]
porcento = [7.5,9,12,14]
desc = [0, 19.8, 96.94, 174.08]

bases_irrf = [2112,2826.65,3751.05,4664.68,1000000]
aliq =    [0, 7.5,   15,    22.5,   27.5  ]
desc_ir = [0, 158.4, 370.4, 651.73, 884.96]

valor_inss=0
global x
x=0
def inss(valor):
    x=0
    for i in bases_inss:
        if valor > 7507.49:
          valor_inss = 876.95
          return valor_inss
        else:
          if valor <= i:
            valor_inss = (valor*porcento[x]/100)-(desc[x])
            return valor_inss
            
          else:
            x += 1
        
def irrf(valor,x):
  x=0
  for i in bases_irrf:
      if valor <= i:
         valor_irrf = (valor*aliq[x]/100)-desc_ir[x]
         print(aliq[x])
         print(desc_ir[x])
         return valor_irrf
      else:
       x += 1
         


