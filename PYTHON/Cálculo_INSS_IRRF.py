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
dep=dep*189.59

#------------------------------------------------------------
basesalario = [1.320, 2571.29, 3856.94, 7507.49]

aliquotainss = [7.5, 9, 12, 14]

deducaoinss = [0, 19.8, 96.94, 174.08]

tetoinss = 876,95

baseir = [2112.01, 2826.66, 3751.06, 5000000]

aliquotair = [7.5, 15, 22.5, 27.5]

parceladeduzir = [158.4, 370.4, 651.73, 884.96]

deducaodependenteir = 189.59

valordeducaoir = deducaodependenteir*dep

print(len(basesalario))
#------------------------------------------------------------
sal=(sal-fal)
fgts=sal*0.08
inss=0
cont = 0
for i in range(cont < len(basesalario)):
    if sal > basesalario[3]:
      int(inss = tetoinss)
      break
    
    else:
        if sal < basesalario[cont]:
            int(inss = (sal*aliquotainss[cont])-parceladeduzir[cont])
            break
    cont = cont+1


print("="*50)
print(f'Valor base do INSS é : {sal:,.2f}')
#--------------------------------------------------------
baseir=sal-(pen+dep+inss)
if baseir<1903.99:
  ir=0
elif baseir<2826.66:
  ir=baseir*0.075-142.8
elif baseir<3751.06:
  ir=baseir*0.15-354.8
elif baseir<4664.69:
  ir=baseir*0.225-636.13
else:
  ir=baseir*0.275-869.36

print(f'O valor do INSS será..: {inss:,.2f}')
print("="*50)
print(f'O Valor do FGTS é ....: {fgts:,.2f}')
print("="*50)
print(f'O Base do IRRF  é ....: {baseir:,.2f}')
print(f'O valor do IRRF é ....: {ir:,.2f}')
print("="*50)