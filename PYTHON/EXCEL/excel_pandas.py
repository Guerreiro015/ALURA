
import os
os.system("cls" or None)

import pandas as pd

tabela = pd.read_excel("dados.xlsx")
tabela.drop(index = 0)

print(tabela.head())
print(tabela)


##################################################
