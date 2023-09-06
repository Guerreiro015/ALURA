import os
os.system('cls')

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

cores = []

df = pd.read_excel('CUSTO0823.xlsx')

df=pd.DataFrame(df)

fol=list(df['Folha'])
sin=list(df['Siemaco'])
dd={'Folha': fol, 'Sindicato': sin}
dados=pd.DataFrame(dd)

print(dados)



#df.set_index('Folha',inplace=True) # Colocar o culuna pais como indice

#Ordenando do Maior para o menor e pegando os 10 peimeiros
#top10=df.sort_values('Total',ascending=False).head(10) 
#print(top10)
fig,ax = plt.subplots(figsize=(10,4))
ax.plot(dados['Folha'], dados['Sindicato'])
# ax.plot(data=df, y='Folha', x='Steriiisp')
# ax.plot(data=df, y='Folha', x='Selur')

ax.set(title='Salários por Regionais',xlabel='Valor Salários',ylabel='Regionais')


plt.show()
