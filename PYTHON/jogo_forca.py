def forca():
    import titulo_menu
    import os
    os.system('cls') or None

    print('*****************************************')
    print('****** Bem-vindo ao jogo da Forca *******')
    print('*****************************************')

    index = 0
    palavra = "maracuja"
    tamanho = len(palavra)
    lista = []
    for i in range(tamanho):# adiconar _ na lista
        lista.append("_")
        
    tentativa = 1
    palavra = palavra.upper()# Transformar em maisculos
    palavra = palavra.lower()# Transformar em minúsculo
    palavra = palavra.strip() # tira espaços no inicio e fim
    #palavra = palavra.capitalize() # Primeira letra em maiúscula
    #o funcao " ".join serve para imprimir um lista sem os colchetes
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
                lista[index] = chute
                print(f" A letra  digitada foi encontrada na posição ( {index} )")
                print(" ".join(lista))
                input('')            
                index=index+1
                
            else:
                index=index+1
           
        tentativa = tentativa + 1
        index=0   
    print("="*50)
    print(f"PARABENS, voce acertou em {tentativa} tentativas \n")  
    print(f"A palavra é {palavra.upper()}")
    print("="*50)
    print("\n Fim do jogo\n")
        

if(__name__ == '__main__'):
    forca()