import random
import os
os.system('cls') or None

# Vamos puxar uma função criada em outro programa
import titulo_menu # importando um programa voce pode usar suas funcoes
titulo_menu.menu() # usando funcao que esta no programa titulo_menu

def jogo1():
    import advinhacao_randon # executando este programa
def jogo2():
    import Advinhacao_while # executando este programa
def jogo3():
    import jogo_forca # executando este programa
def jogo4():
    import Cálculo_INSS_IRRF # executando este programa


cont = True

while cont == True:
    os.system("cls" or None)
    print("*"*50)
    print("****  MENU DOS JOGOS DE ADVINHAR!  *****".center(50))
    print("*"*50)

    print("-"*50)
    print('Escolha abaixo qual jogo deseja jogar'.center(50))
    print("-"*50)
    print("\n (1) - Advinhação Random *** (2) - Advinhação com While ")
    print("\n (3) - Jogo da Forca  ****** (4) - Cáculo de INSS e IRRF")
    print("-"*50)

    opcao = input("\n Escolha qual jogo você quer jogar ..: ")

    if opcao == "":
        continue
    opcao = int(opcao)
    if opcao == 1:
        jogo1()
    elif opcao == 2:
        jogo2()
    elif opcao == 3:
        jogo3()
    elif opcao == 4:
        jogo4()

    else:
        print("Opçâo inválida, Tchau")
        break

        

