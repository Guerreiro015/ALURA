import os
os.system("cls" or None)

import openpyxl

# ABRIR UM ARQUIVO EXSITENTE

plan = openpyxl.Workbook('teste.xlsx')

print(plan.sheetnames)
planilha = plan["frutas"]
