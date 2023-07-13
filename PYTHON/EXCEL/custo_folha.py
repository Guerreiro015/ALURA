import os
os.system("cls" or None)

import pandas as pd



tb = pd.read_excel("FOLHA05.xlsx")
print(tb[["Id Contratado","Nome","Cargo"]]) # para selecionar os campos para ver usas colchetes duplos
 
 
#INSERIR UMA COLUNA USANDO Parmetros ( nº coluna,nome coluna, valor da coluna)
tb.insert(6,"Selur", tb["4Salário - Mensalistas"]*0.5/100)
tb.insert(6,"Steriiisp", 0)
tb.insert(6,"Siemaco", 0)

tb.insert(9,"Inss",0)

#Alterar dados da planilha
tb.loc[tb["Sindicato"] == "SIEMACO SAO PAULO LIMP URBANA","Siemaco"] = tb["4Salário - Mensalistas"]*0.6/100
print(tb[["Id Contratado","Nome","Siemaco","Steriiisp"]])

tb.loc[tb["Sindicato"] == "SIND TRAB EMP DE ONIBUS RODOV INTEREST INTERM SET DIF SAO PAULO","Steriiisp"] = tb["4Salário - Mensalistas"]*0.4/100
print(tb[["Id Contratado","Nome","Siemaco","Steriiisp"]])


tb.to_excel("CUSTO05.xlsx",index=False)

nova = pd.read_excel("CUSTO05.xlsx")
print("\n------  Cálculos dos sindicatos feito e OK.....  \n")
