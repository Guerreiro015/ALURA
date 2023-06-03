def linha():
  print("="*50)

print("="*50)
print("-"*50)
print("CÁLCULO DE INSS - FGTS - IRRF ".center(50))
print("-"*50)
print("="*50)
sal=int(input('Digite o valor do Salário........ ..: '))
fal=int(input('Digite Valor das faltas e atrasos. .: '))
pen=int(input('Digite o valor da Pensão............: '))
dep=int(input('Digite a Quant. de Dependentes. IR..: '))

tetoinss = 876.95
dep=dep*189.59
deducao_simplicada = 528.00

#------------------------------------------------------------
basesalario = [0,1320, 2571.29, 3856.94, 7507.49]

aliquotainss = [7.5, 9, 12, 14]

deducaoinss = [0, 19.8, 96.94, 174.08]

#-----------------------------------------------------
baseir = [2112.01, 2826.66, 3751.06, 4664.68,5000000]

aliquotair = [0,7.5, 15, 22.5, 27.5]

parceladeduzir = [0,158.4, 370.4, 651.73, 884.96]

deducaodependenteir = 189.59

valordeducaoir = deducaodependenteir*dep

#------------------------------------------------------------
sal=(sal-fal)
fgts=sal*0.08
inss=0
cont = 0


for i in range(cont,len(basesalario)):
      if sal > basesalario[4]:
        inss = tetoinss
        break
      
      if (sal > basesalario[cont] and sal < basesalario[cont+1]):
        inss = (sal*(aliquotainss[cont]/100))-deducaoinss[cont]
        break
      else:
        cont = cont+1
print(aliquotainss[cont])
print(deducaoinss[cont])
print("="*50)
print(f'Valor base do INSS é : {sal:,.2f}')
print(f'O valor do INSS será..: {inss:,.2f}')
print("="*50)
#--------------------------------------------------------
#--------------------------------------------------------

base_deducao_ir = (pen+dep+inss)
cont = 0
for i in range(cont,len(baseir)):
  if (base_deducao_ir < deducao_simplicada):
          base_deducao_ir = deducao_simplicada
    
  salarioir=sal-base_deducao_ir

  if salarioir<baseir[0]:
    ir=0
    break
  
  if salarioir < baseir[cont]:
    ir=(salarioir*(aliquotair[cont]/100)) - parceladeduzir[cont]
    break
  else:
    cont=cont+1

print(base_deducao_ir)
print(aliquotair[cont])
print(parceladeduzir[cont])



print(f'O Valor do FGTS é ....: {fgts:,.2f}')
print("="*50)
print(f'O Base do IRRF  é ....: {salarioir:,.2f}')
print(f'O valor do IRRF é ....: {ir:,.2f}')
print("="*50)