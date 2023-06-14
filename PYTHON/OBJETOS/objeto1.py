numero = 123
titular = "Nico"
saldo = 55.0
limite = 1000.0
conta = {"numero": 123, "titular": "Nico", "saldo": 55.0, "limite": 1000.0}

conta2 = {"nunero": 222, "titular": "Anto", "saldo": 100, "limite": 1000.0}

def cria_conta(num,nom,sal,lim):
     conta = {"numero": num, "titular": nom, "saldo": sal, "limite": lim}
     return conta

def deposita(conta,valor):
     conta["saldo"] += valor

def saca(conta,valor):
     conta["saldo"] -= valor

def estrato(conta,valor):
     print(saldo)







