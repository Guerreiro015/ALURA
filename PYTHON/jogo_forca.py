def forca():
    import titulo_menu
    import os
    os.system('cls') or None

    print('*****************************************')
    print('****** Bem-vindo ao jogo da Forca *******')
    print('*****************************************')

    posicao = 0
    palavra = "coco"
    tamanho = len(palavra)
    lista = []
    for i in range(tamanho):# adiconar _ na lista
        lista.append("_")
        
    tentativa = 1
    palavra = palavra.upper()# Transformar em maisculos
    palavra = palavra.lower()# Transformar em minúsculo
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
        print("\n Acerte a palavra acima...")
        chute = input(f"{tentativa}ª Tentativa,  Qual o seu chute? ")

        chute = chute.strip()
        chute = chute.lower()
        if chute not in(fruta):
           print(f"A letra digitada, não tem na palavra secreta") 
           tentativa = tentativa + 1
           input('')
           continue
        for letra in (palavra):
            if (chute.lower() == letra.lower()):
                lista[posicao] = chute
                print(f" A letra  digitada foi encontrada na posição ( {posicao} )")
                print(" ".join(lista))
                input('')            
                posicao=posicao+1
                
            else:
                posicao=posicao+1
           
        tentativa = tentativa + 1
        posicao=0   
    print("="*50)
    print(f"PARABENS, voce acertou em {tentativa} tentativas \n")  
    print(f"A palavra é - {palavra.upper()} -".center(50))
    print("="*50)
    print("\n Fim do jogo\n")
        

if(__name__ == '__main__'):
    forca()