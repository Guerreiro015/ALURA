import os
os.system("cls" or None)

import pandas as pd



tabela = pd.read_excel("FOLHA05.xlsx")
print(tabela[["Id Contratado","Nome","Cargo"]]) # para selecionar os campos para ver usas colchetes duplos
 
 
#INSERIR UMA COLUNA USANDO Parmetros ( nº coluna,nome coluna, valor da coluna)
tabela.insert(6,"Selur", tabela["4Salário - Mensalistas"]*0.5/100)
tabela.insert(6,"Steriiisp", 0)
tabela.insert(6,"Siemaco", 0)

#Alterar dados da planilha
tabela.loc[tabela["Sindicato"] == "SIEMACO SAO PAULO LIMP URBANA","Siemaco"] = tabela["4Salário - Mensalistas"]*0.6/100
print(tabela[["Id Contratado","Nome","Siemaco","Steriiisp"]])

tabela.loc[tabela["Sindicato"] == "SIND TRAB EMP DE ONIBUS RODOV INTEREST INTERM SET DIF SAO PAULO","Steriiisp"] = tabela["4Salário - Mensalistas"]*0.4/100
print(tabela[["Id Contratado","Nome","Siemaco","Steriiisp"]])


tabela.to_excel("CUSTO05.xlsx",index=False)

nova = pd.read_excel("CUSTO05.xlsx")
print("\n------  Cálculos dos sindicatos feito e OK.....  \n")
