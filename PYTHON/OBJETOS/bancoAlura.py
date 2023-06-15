import os
os.system("cls")

from base_banco import banco

cliente3 = banco("Luana",333,50, 80)

print(f" A cliente {cliente3.nome} abriu uma com com R$: {cliente3.saldo}\n")

deposito_cliente3 = int(input(f"Digite o valor do deposito para {cliente3.nome}: R$: "))

cliente3.deposito(deposito_cliente3)

print(f"O cliente {cliente3.nome} depositou R$: {deposito_cliente3} e ficou com R$: {cliente3.saldo} de saldo\n")# verificando o saldo


gato = banco("Romeu",444,630,1000)
print (f"O cliente {gato.nome} abriu a conta com R$: {gato.saldo}")

deposito_gato = int(input(f"Digite o valor de dposito para {gato.nome} R$: " ))

gato.deposito(deposito_gato)

print(f"O cliente {gato.nome} fez um deposito de R$: {deposito_gato} e seu saldo agora é {gato.saldo} \n")

 




