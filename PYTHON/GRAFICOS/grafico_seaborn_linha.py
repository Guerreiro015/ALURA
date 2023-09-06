import os
os.system('cls')

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('imigrantes.csv')
print(df)


df.set_index('País',inplace=True) # Colocar o culuna pais como indice
print(df)


anos=list(map(str,range(1980,2014))) # Crianndo uma lista com os anos como strings
print(anos)

#Extração da série de dados para o Brasil
#criamos uma variável chamada brasil igual à df.loc[]
# e variável anos nos colchetes.

paises=df.loc[['Brasil','Argentina','Cuba','Peru'],anos] #Vamos usar dois paises

paises=paises.T # Trocar horizontal por vertical

print(paises)

# VAMOS USAR MAIS DE UMA INFORMAÇÃO
import matplotlib.pyplot as plt

sns.set_theme(style='dark')

fig, ax = plt.subplots(figsize=(10, 5))
ax = sns.lineplot(df.loc['Brasil', anos], label='Brasil', lw=4)
ax = sns.lineplot(df.loc['Argentina', anos], label='Argentina', lw=3)
ax = sns.lineplot(df.loc['Peru', anos], label='Peru', lw=3)
ax = sns.lineplot(df.loc['Colômbia', anos], label='Colômbia', lw=3)

ax.set_title('Imigração dos maiores países da América do Sul\npara o Canadá de 1980 a 2013', loc='left', fontsize=20)
ax.set_xlabel('Ano', fontsize=14)
ax.set_ylabel('Número de imigrantes', fontsize=12)

ax.xaxis.set_major_locator(plt.MultipleLocator(5))

#ax.legend(title='Países', loc='upper right', bbox_to_anchor=(0.2, 1.0)) # Posição da legenda

plt.show()