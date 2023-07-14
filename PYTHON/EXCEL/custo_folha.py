import os
os.system("cls" or None)

import pandas as pd

abrir = input("Digite o nome do arquivo origem. : ").upper()
novo = input("Digite o nome do arquivo a ser criado. : ").upper()
abrir = (abrir+".xlsx")
novo_arquivo = (novo+".xlsx")

# abrir = "FOLHA06.xlsx"
# novo_arquivo = "custo06.xlsx"

tb = pd.read_excel(abrir)
print(tb[["Id Contratado","Nome","Cargo"]]) # para selecionar os campos para ver usas colchetes duplos
 
 
#INSERIR UMA COLUNA USANDO Parmetros ( nº coluna,nome coluna, valor da coluna)
tb.insert(7,"Selur", tb["4Salário - Mensalistas"]*0.5/100)
tb.insert(7,"Steriiisp", 0)
tb.insert(7,"Siemaco", 0)


#Alterar dados da planilha
tb.loc[tb["Sindicatos"] == "SIEMACO SAO PAULO LIMP URBANA","Siemaco"] = tb["4Salário - Mensalistas"]*0.6/100
print(tb[["Id Contratado","Nome","Siemaco","Steriiisp"]])

tb.loc[tb["Sindicatos"] == "SIND TRAB EMP DE ONIBUS RODOV INTEREST INTERM SET DIF SAO PAULO","Steriiisp"] = tb["4Salário - Mensalistas"]*0.4/100

print(tb[["Id Contratado","Nome","Siemaco","Steriiisp"]])

tb.insert(10,"Inss",(tb["1001Base INSS 13º Salário"]+tb["1007Base do INSS Normal"]+tb["1008Base do INSS Normal Excedente"]+tb["1031Base INSS/FGTS Férias do Mês"])*28.9854/100)

tb.insert(10,"Fgts",(tb["1005Base do FGTS Normal"]+tb["1010Base do FGTS 13º Salário"]+tb["1031Base INSS/FGTS Férias do Mês"])*8/100-tb["1039Valor do FGTS - GRFF"])

tb.loc[tb["Cargo"] == "MENOR/JOVEM APRENDIZ","Fgts"] = tb["15Salário Aprendiz - Mensalistas"]*2/100

tb.loc[tb["Situação"] == "Licença-Maternidade","Inss"] = 0





tb.to_excel(novo_arquivo,index=False)

nova = pd.read_excel(novo_arquivo)
print("\n------  Montagem da Planilha de custos Mensais Feito com Sucesso e OK.....  \n")
