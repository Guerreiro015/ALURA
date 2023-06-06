def forca():
    import os
    os.system('cls') or None

    print('*****************************************')
    print('****** Bem-vindo ao jogo da Forca *******')
    print('*****************************************')

    index = 0
    palavra = " BANANA   "
    lista = ["_","_","_","_","_","_",]

    palavra = palavra.upper()# Transformar em maisculos
    palavra = palavra.lower()# Transformar em minúsculo
    palavra = palavra.strip() # tira espaços no inicio e fim
    palavra = palavra.capitalize() # Primeira letra em maiúscula
     


    enforcou = False
    acertou = False
    while(not enforcou and not acertou):
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
    
        index=0   
        acertou = False
    print("Fim do jogo")
        

if(__name__ == '__main__'):
    forca()