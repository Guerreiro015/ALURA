numero = 123
titular = "Nico"
saldo = 55.0
limite = 1000.0
conta = {"numero": 123, "titular": "Nico", "saldo": 55.0, "limite": 1000.0}

conta2 = {"nunero": 222, "titular": "Anto", "saldo": 100, "limite": 1000.0}

def cria_conta(num,nom,sal,lim):
     conta = {"numero": num, "titular": nom, "saldo": sal, "limite": lim}
     return conta

# teste = cria_conta(123,"antonio",1500,5000)
# print(teste)

def deposito(conta,valor):
     conta["saldo"] += valor
     

def saque(conta,valor):
     conta["saldo"] -= valor
     
def extrato(conta):
  print(f"O saldo a conta é {conta[saldo]}")







