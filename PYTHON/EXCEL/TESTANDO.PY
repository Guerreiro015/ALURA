import os
os.system("cls" or None)

import pandas as pd


nova = pd.read_excel("FOLHA05.xlsx")

colunas = len(nova.columns)
colunas2 = nova.shape[1]
colunas3 = nova.columns

print(colunas)
print(colunas2)
print(colunas3)

if "Nome" in colunas3:
    print(" Existe")
else:
    print("Não Existe")
for x in colunas3:
    
    print(x)



print("\n------  Montagem da Planilha de custos Mensais Feito com Sucesso e OK.....  \n")
