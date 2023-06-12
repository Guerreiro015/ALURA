def palavra_secreta():
    with open("lista_frutas.txt","w") as arquivo:
        arquivo.write("banana\nmelancia\nmanga\nabacaxi\nmaracuja\nmorango\nameixa\ngoiaba\ncaju\npera\ncarambola\nlaranja\ncaqui\nabacate\nmamao\n")

    import random
    with open("lista_frutas.txt","r") as lista:
        ler = lista.readlines()
    tamanho = len(ler)
    numero = random.randrange(0,tamanho)

    palavra = ler[numero]
    return palavra

    print(tamanho)
    print(palavra)
    for linha in ler:
        print(linha)

def perdeu():
               
    print(" você foi enforcado! ".center(50))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

    print("=" * 50)
    print("Fim do jogo".center(50))
    print("=" * 50)


def ganhou():
           
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

    print("=" * 50)          
    print(" Fim do jogo".center(50))
    print("=" * 50)      

if __name__ == "__main__":
    palavra_secreta()

