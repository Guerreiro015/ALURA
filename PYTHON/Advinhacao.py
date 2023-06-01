# This is a sample Python script.
print("*"*50)
print("* Bem vindo ao jogo de Adivinhação *".center(50))
print("*"*50)

num = 42
chute = input("Digite o seu CHUTE ..:  ")
chute = int(chute)
if (chute == num):
    print('Você acertou, o numero foi ',chute)

    print("-"*50)
    print("Fim do jogo ".center(50))
    print("*"*50)
  
elif (chute > num):
    print('\nNão deu, você errou - -  o número é menor....\n')

elif (chute < num):
    print('\nNão deu, você errou - -  o número é maior....\n')
else:
    print('erro desconhecido....')

    



