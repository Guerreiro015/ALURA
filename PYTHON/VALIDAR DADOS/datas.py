import os
os.system('cls')

from datetime import datetime,timedelta
from validar_datas import data_br

cad = data_br()
print(cad.momento)
print(cad.mes_cadastro())
print(cad.dia_cadastro())
print(cad.data_formatada())

print(cad)

print(datetime.today())


