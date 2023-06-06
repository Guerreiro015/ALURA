def forca():
    import os
    os.system('cls') or None

    print('*****************************************')
    print('****** Bem-vindo ao jogo da Forca *******')
    print('*****************************************')

    index = 0
    palavra = "abobora"
    tamanho = len(palavra)
    lista = []
    for i in range(tamanho):
        lista.append("a")
        
    tentativa = 0
    palavra = palavra.upper()# Transformar em maisculos
    palavra = palavra.lower()# Transformar em minúsculo
    palavra = palavra.strip() # tira espaços no inicio e fim
    #palavra = palavra.capitalize() # Primeira letra em maiúscula
     
    banana = list(palavra)
    print(banana,tamanho)

    
    while(banana != lista):
        print(lista[0],lista[1],lista[2],lista[3],lista[4],lista[5],"\n")
        print("Acerte a palavra acima...")
        chute = input("Qual chute? ")
        chute = chute.strip()
        chute = chute.lower()

        for letra in (palavra):
            if (chute.lower() == letra.lower()):
                print(f"A letra ( {letra} ) digitada foi encontrda na posição ( {index} )")
                lista[index] = chute
                index=index+1
                
            else:
               # print(f"A letra ( {chute}) digitada, não tem na palavra secreta")
                index=index+1
                continue
    
        tentativa = tentativa + 1
        index=0   

    print(f"Parabeens voce acertou em {tentativa} tentativas \n")  
    print(f"A palavra era {palavra} \n")
    print("Fim do jogo")
        

if(__name__ == '__main__'):
    forca()