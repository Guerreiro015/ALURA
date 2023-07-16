import os
os.system("cls" or None)

import pandas as pd


nova = pd.read_excel("FOLHA05.xlsx")

colunas = len(nova.columns)
colunas2 = nova.shape[1]
campos = nova.columns

print(colunas)
print(colunas2)
print(campos)

if "Nome" not in campos:
    print(" Existe")
else:
    print("Não Existe")
# for x in campos:
    
#     print(x)

print(type(campos))

if "1001Base INSS 13º Salário" not in campos:
    1001Base INSS 13º Salário = 0


print("\n------  Montagem da Planilha de custos Mensais Feito com Sucesso e OK.....  \n")
