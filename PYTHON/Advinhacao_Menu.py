import os
os.system('cls') or None

# Vamos puxar uma função criada em outro programa
import titulo_menu # importando um programa voce pode usar suas funcoes
titulo_menu.menu() # usando funcao que esta no programa titulo_menu

def jogo1():
    import Advinhacao_Randon # executando este programa
def jogo2():
    import Advinhacao_While # executando este programa


import random

print("*"*50)
print("****  MENU DOS JOGOS DE ADVINHAR!  *****".center(50))
print("*"*50)

cont = True

while cont == True:

    print("-"*50)
    print('Escolha abaixo qual jogo deseja jogar'.center(50))
    opcao = input("\n (1) - ADVINHACAO RANDOM (2) - ADVINHACAO WHILE  " )
    if opcao == "":
        continue
    opcao = int(opcao)
    if opcao == 1:
        jogo1()
    elif opcao == 2:
        jogo2()
    else:
        print("Opçâo inválida, Tchau")
        break

        

