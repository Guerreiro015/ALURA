import os
os.system("cls" or None)

import pandas as pd


nova = pd.read_excel("FOLHA06.xlsx")

colunas = len(nova.columns)
colunas2 = nova.shape[1]
campos = nova.columns

print(colunas)
print(colunas2)
print(campos)

if "7Salário-Maternidade" in campos:
    print("Licença-Maternidade in campos: Existe SIM")
    print(nova[["Id Contratado","Nome","Cargo"]])
else:
    print("Licença-Maternidade in campos:Não Existe")
    print(nova[["Id Contratado","Nome","Situação"]])




# for x in campos:
    
#     print(x)

# print(type(campos))

# if "1001Base INSS 13º Salário" not in campos:
#     nova.insert(10,"1001Base INSS 13º Salário", 0)

    
# nova.to_excel("teste.xlsx",index=False)

# nova = pd.read_excel("teste.xlsx")
# print(nova["Id Contratado"],["1001Base INSS 13º Salário"])
# print("\n------  Montagem da Planilha de custos Mensais Feito com Sucesso e OK.....  \n")

