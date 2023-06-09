def forca():
    import titulo_menu
    import os
    os.system('cls') or None
    titulo_menu.menu()
    
    posicao = 0
    palavra = "maracuja".upper()
    tamanho = len(palavra)
    lista = []
    for i in range(tamanho):# adiconar _ na lista
        lista.append("_")
        
    tentativa = 1
    palavra = palavra.lower()# Transformar em maisculos
    palavra = palavra.upper()# Transformar em minúsculo
    palavra = palavra.strip() # tira espaços no inicio e fim
    
    #palavra.index(item, inicio, fim) Para saber a posicao de um item dentro da lista

    #palavra = palavra.capitalize() # Primeira letra em maiúscula

    #A funcao " ".join serve para imprimir um lista sem os colchetes

    #A função .count() contar o número de ocorrências de um determinado elemento em uma lista.

    fruta = list(palavra)
    print(" ".join(fruta),tamanho)

    
    while(fruta != lista):
        os.system('cls') or None
        titulo_menu.menu()

        print(" ".join(lista))
        print("\nAcerte a palavra acima...")
        print('-'*50)
        chute = input(f"{tentativa}ª Tentativa,  Qual o seu chute? ")
        print('-'*50)

        chute = chute.strip().upper()
        
        if chute not in(fruta):
           print(f"A letra digitada, não tem na palavra secreta") 
           tentativa += 1
           input('')
           continue
        for letra in (palavra):
            if (chute.upper() == letra.upper()):
                lista[posicao] = chute
                print(f" A letra  digitada foi encontrada na posição ( {posicao} )")
                print(" ".join(lista))
                input('')            
                posicao += 1
                
            else:
                posicao=posicao+1
           
        tentativa += 1
        if tentativa > 5:
            print("="*50)
            print(f"INFELIZMENTE, voce NÃO acertou nas {tentativa-1} tentativas \n")  
            print(f"A palavra é - {palavra.upper()} -".center(50))
            print("="*50)
            print("\n Fim do jogo\n")
            fruta == lista
        else:
            posicao=0   
    print("="*50)
    print(f"PARABENS, voce acertou em {tentativa-1} tentativas \n")  
    print(f"A palavra é - {palavra.upper()} -".center(50))
    print("="*50)
    print("\n Fim do jogo\n")
        

if(__name__ == '__main__'):
    forca()