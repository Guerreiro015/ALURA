import os
os.system('cls')

import pandas as pd

df = pd.read_csv('imigrantes.csv')
print(df)

df.set_index('Country',inplace=True) # Colocar o culuna pais como indice
print(df)

anos=list(map(str,range(1980,2014))) # Crianndo uma lista com os anos como strings
print(anos)

#Extração da série de dados para o Brasil
#criamos uma variável chamada brasil igual à df.loc[]
# e variável anos nos colchetes.


brasil = df.loc['Brasil', anos]

print(brasil)