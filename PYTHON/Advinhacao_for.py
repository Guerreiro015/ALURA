
def listra(): 
    print ("*"*50) 

listra()
print("* Bem vindo ao jogo de Adivinhação *".center(50))
listra()

num = 42
chance = 1
for i in range(chance, 10):
    chute = input("Digite o seu CHUTE ..:  ")
    chute = int(chute)
    if (chute == num):
        print('Você acertou, na chance {}, o numero é '.format(chance),chute)

        listra()
        print("Fim do jogo ".center(50))
        listra()
        break

    elif (chute > num):
        listra()
        print('\n A Chance {}, chute {} Não deu, você errou - -  o número é MENOR\n'.format(chance,chute))
        listra()
        chance = chance+1

    elif (chute < num):
        listra()
        print('\n A Chance {}, chute {} Não deu, você errou - -  o número é MAIOR\n'.format(chance,chute))
        listra()
        chance = chance+1

    else:
        print('erro desconhecido....')
    



