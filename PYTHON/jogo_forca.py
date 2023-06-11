def forca():
    import titulo_menu
    import random
    import palavra_forca
    import os

    os.system("cls") or None
    titulo_menu.menu()

    def perdeu():
        print("=" * 50)
        print(f"INFELIZMENTE, voce NÃO acertou nas {tentativa-1} tentativas \n")
        print(f"A palavra é - {palavra.upper()} -".center(50))
        print("=" * 50)
        
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

        print("Fim do jogo".center(50))
        print("=" * 50)
        fruta == lista
    def ganhou():
            print("=" * 50)

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
            print(f"PARABENS, voce acertou em {tentativa} tentativas".center(50))
            print(f"A palavra é - {palavra.upper()} -".center(50))
            print("=" * 50)
            print(" Fim do jogo".center(50))
            print("=" * 50)

   # SELECIONANDO PALAVRA
   #============================================
    palavra = palavra_forca.palavra_secreta()
   #==============================================
    posicao = 0
    digitada = []
    #palavra = "abacaxi".upper()
    tamanho = len(palavra)
    lista = []

   

    for i in range(tamanho-1):  # adiconar _ na lista
        lista.append("_")


    tentativa = 0
    palavra = palavra.lower()  # Transformar em maisculos
    palavra = palavra.upper()  # Transformar em minúsculo
    palavra = palavra.strip()  # tira espaços no inicio e fim

    # palavra.index(item, inicio, fim) Para saber a posicao de um item dentro da lista

    # palavra = palavra.capitalize() # Primeira letra em maiúscula

    # A funcao " ".join serve para imprimir um lista sem os colchetes

    # A função .count() contar o número de ocorrências de um determinado elemento em uma lista.

    fruta = list(palavra)
    print(" ".join(fruta), tamanho)

    while fruta != lista:
        tentativa += 1
        if tentativa > 10:
            perdeu()
            break
        os.system("cls") or None
        titulo_menu.menu()

        print("LETRAS ACERTADAS =>  ", " ".join(lista))
        print("LETRAS CHUTADAS  =>  ", " ".join(digitada))
        print("\nAcerte a palavra acima...")
        print("-" * 50)
        chute = input(f"{tentativa}ª Tentativa,  Qual o seu chute? ")
        print("-" * 50)
        chute = chute.strip().upper()
        digitada.append(chute)

        if chute not in (fruta):
            print(f"A letra digitada, não tem na palavra secreta")
            input("")
            continue

        for letra in palavra:
            if chute.upper() == letra.upper():
                lista[posicao] = chute
                print(f" A letra  digitada foi encontrada na posição ( {posicao} )")
                print(" ".join(lista))
                input("")
                posicao += 1

            else:
                posicao += 1
        if fruta == lista:
          ganhou()
          break  
        # tentativa += 1

        posicao = 0

       

if __name__ == "__main__":
    forca()
